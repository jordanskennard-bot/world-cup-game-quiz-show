# Closing Credits — Instructions for Claude Code

## Context: this already half-exists

Don't build this from scratch. `host-complete_42.html` already has an end-of-game
system called `FoulPlayFinale` (search for `window.FoulPlayFinale`, defined around
line 9892, and its trigger `buildFinaleStory` / `showVictoryScreen` around line
8151). It already:

- Fires automatically after `showVictoryScreen()` (final whistle → fanfare →
  full-time commentary), or via the "🎬 Play the Highlight Reel" button.
- Generates an AI song with ElevenLabs' Music API
  (`POST https://api.elevenlabs.io/v1/music`, `xi-api-key` header, body
  `{ prompt, music_length_ms }`, `Accept: audio/mpeg`) and picks one of **3
  random styles** for it.
- Builds a lyric brief from game data via `buildFinaleStory(data, ctx)`
  (winner/margin, MVP, scoreline swings, one or two named round moments).
- Collects photos from Firebase (`finaleImages`, `players/*/photo`,
  `blowBall/photos`) and renders them as a slideshow on a canvas synced to the
  song, then records it to video with `MediaRecorder` (download/share buttons
  included).

So this task is a **modification** of `FoulPlayFinale`, not a new feature. Read
the whole IIFE (roughly lines 9892–10230+) before changing anything — it's a
single self-contained module.

## What's changing

1. **Genre: 3 fixed styles → rap / rock / folk, randomised per game.**
2. **Length: 30 seconds → 60 seconds.**
3. **Photos: broaden the montage** beyond profile pics + blow-ball snaps to
   cover the rounds that don't currently feed images in.
4. **Lyrics: make "who did well at key points" actually true** — a couple of
   the fields the lyric-builder already reads are never written anywhere, so
   fix those, and add a few more round outcomes as lyric material.

Go through each of the four below in order.

---

## 1. Genre: rap / rock / folk

Find the `STYLES` array near the top of the `FoulPlayFinale` IIFE:

```js
const STYLES = [
  'a rousing Britpop singalong anthem...',
  'a soaring power ballad...',
  'a high-energy hip-hop hype anthem...'
];
```

Replace it with three genre-specific style prompts — describe the *sound*,
don't name real artists or bands (ElevenLabs' music generation should not be
prompted with real-artist names):

```js
const STYLES = [
  {
    genre: 'rap',
    text: 'a confident old-school boom-bap hip-hop hype track, punchy rapped verses '
        + 'with a tight flow, scratch-style ad-libs, and a loud chantable hook'
  },
  {
    genre: 'rock',
    text: 'an anthemic football-terrace rock song, crunchy electric guitars, driving '
        + 'drums, a massive singalong chorus built for a crowd of mates shouting it back'
  },
  {
    genre: 'folk',
    text: 'a warm acoustic folk singalong, fingerpicked or strummed acoustic guitar, '
        + 'stomping foot-percussion, and a group of voices joining in on the chorus'
  }
];
```

Update `F.buildPrompt` to pick one entry and use `.text` in the prompt string
(keep a reference to which `.genre` got picked — you'll want it for the
composition plan in step 4, and it's worth logging/storing on the game record
so the host can see which one they got, e.g.
`gameRef.child('finaleStory/songGenre').set(style.genre)`).

---

## 2. Length: 60 seconds

- Change `TARGET_MS` from `30000` to `60000`.
- Search the whole IIFE for every other place `30` / `30000` / `TARGET_MS` is
  used for timing — the render loop (`F._render`, uses `DUR`), the
  `MediaRecorder` stop timer, and any `setTimeout` that assumes a 30s clip
  (e.g. the `launchFinaleReel` auto-roll timer in `showVictoryScreen`, and any
  fixed-length fallback in `FALLBACK_SONG` playback). All of these need to
  derive from the same constant, not have `30000`/`30` hardcoded separately —
  audit this rather than assuming the constant does all the work.
- `music_length_ms` on the compose call is valid from 3,000–600,000 ms, so
  60,000 is fine as-is.
- With double the runtime, `F._render`'s `INTRO`/`OUTRO` (currently 3s each)
  can stay the same; the per-image slideshow duration (`midDur`, `per`) will
  automatically stretch since it's computed from `DUR - INTRO - OUTRO`. Just
  confirm the crossfade math (`XF`) still looks reasonable with more images —
  test with a game that has 8–10 photos.

---

## 3. Broaden the photo montage

Current `F.collectImages` only pulls from `finaleImages` (AI face-swap
portraits), `players/*/photo` (profile pics), and `blowBall/photos`. The user
wants "photos taken throughout the game — profile pics and for rounds," so:

- **Match Draw round**: currently only `matchDraw/drawingTimeLeft` is tracked
  in Firebase — the actual drawings (canvas data URLs) aren't persisted
  anywhere. Find where each player's drawing is submitted/rendered (search
  `matchDraw` for the drawing-submission handler) and add a write, e.g.
  `gameRef.child('matchDraw/drawings').push({ playerId, dataUrl, chain })`.
  Then add these to `collectImages`.
- **Caption Contest**: reuses the blow-ball photos as its source images
  (`window._captionPhotos`, seeded from blow-ball photos) — these are already
  covered via `blowBall/photos`, so no new source needed there, but consider
  whether to include the *captioned* mockup (photo + winning caption
  overlaid) rather than the bare photo — that's more visually interesting for
  a montage and shows off a round highlight. If you do this, render the
  mockup to an offscreen canvas at the point a caption wins and store that
  composited image (e.g. `finaleImages` with a `source: 'caption'` tag) rather
  than trying to recreate the DOM styling later.
- **Blow Ball**: already covered, no change needed — just confirm nothing
  regressed.
- **Commentary Round / Team Talk / Sabotage reveals**: no photos exist for
  these currently and there's no natural "snap a picture" moment — leave them
  as lyric-only content (see step 4), don't try to synthesize fake images for
  them.
- De-duplicate and order the final array sensibly: team/profile photos first
  (so viewers recognise who's who early), then round photos roughly in game
  order, then any AI face-swap portraits or MVP shot near the end. `seen` /
  `add()` already de-dupes by URL — just control the order you call `add()` in.

---

## 4. Fix and expand the lyric data (`buildFinaleStory`)

Two fields `buildFinaleStory` reads are **dead code today** — they're checked
but nothing ever writes them, so those beats never fire:

- `story.punKing` — the actual write happens as a *top-level* field
  (`gameRef.update({ punKingImageUrl, punKingName })`, around line 4384), not
  under `finaleStory`. Add `gameRef.child('finaleStory/punKing').set(player.name)`
  alongside that existing update (and clear it alongside the existing
  `punKingImageUrl: null` reset, if the round can be replayed).
- `story.karaokeTeam` — there's no tracking of this at all. Find wherever the
  karaoke bonus round is judged/scored and add
  `gameRef.child('finaleStory/karaokeTeam').set(teamName)` when it's decided.

Then add a few more round outcomes as new `finaleStory/*` fields, written at
the point each round concludes, and a matching `beats.push(...)` line in
`buildFinaleStory` for each:

- **Team Talk**: which team scored higher / the single highest-value word
  guessed correctly and by whom.
- **Interview Round**: the player whose answer won the most votes (and which
  question it was for).
- **Match Draw**: the winning chain and/or the player who got the "harder"
  prompt and pulled it off.
- **Blow Ball**: which team scored the +17 first-to-score bonus, and/or the
  team photographer.
- **Sabotage Reveals**: the player who most memorably completed (or spectacularly
  failed) their secret challenge.

Keep beats short, factual, name-first sentence fragments (matching the existing
style, e.g. `"Maria was crowned the Pun King for the best gag"`) — they get
joined into the prompt text, not written verbatim as lyrics, so they should
read as facts to weave in, not finished lines.

With 60 seconds of song instead of 30, raise the beat cap in `F.buildPrompt`
from `.slice(0, 6)` to around `.slice(0, 10)` so the extra round outcomes
actually get used.

### Optional but recommended: switch from `prompt` to `composition_plan`

The current approach sends one big free-text `prompt` and lets the model
freely decide song structure. For a 60-second song where you specifically want
"who did well at key points" to land in the right place, it's worth using
ElevenLabs' **composition plan** instead of a bare prompt, so you can pin
facts to specific sections:

1. `POST https://api.elevenlabs.io/v1/music/plan` with a short prompt to get a
   draft plan back (this call is free, no credits used).
2. Edit the returned plan's `sections` (e.g. `Intro` / `Verse 1` / `Chorus` /
   `Verse 2` / `Chorus` / `Outro`) so their `duration_ms` sum to ~60,000, and
   inject your curated beats into the `lines` of `Verse 1` / `Verse 2` (early
   round moments, MVP, standout plays) and put the winner + scoreline in the
   `Chorus` (repeated, so it's the hook).
3. Set `positive_global_styles` from the chosen genre (e.g. for rap:
   `["rap", "hip-hop", "boom bap"]`; rock: `["rock", "anthemic", "electric guitar"]`;
   folk: `["folk", "acoustic", "group vocals"]`).
4. `POST https://api.elevenlabs.io/v1/music/compose-detailed` (or the
   equivalent compose endpoint) with `{ composition_plan, model_id: "music_v1" }`
   instead of `{ prompt, music_length_ms }`.

This is more work than the current one-shot `prompt` call, so treat it as a
stretch goal — the simpler fix (steps 1–3 above, keeping the plain `prompt`
approach) already gets you a working 60s rap/rock/folk closing-credits song
with more facts baked in. Only do the composition-plan rewrite if the
plain-prompt version doesn't reliably place the facts where you want them
after a few test games.

---

## 5. Naming (cosmetic, do last)

The user calls this "closing credits." The button currently says "🎬 Play the
Highlight Reel." Consider renaming the button/copy to something like "🎶 Play
the Closing Credits" and adjusting the helper text ("A 60-second song about
tonight's match, with a montage of the game — download & share it.") — purely
copy, no functional change. Keep the internal `FoulPlayFinale` name/API as-is
unless you have a reason to rename the module too.

---

## 6. Testing checklist

- [ ] Play through (or mock) a full game with both teams populated, several
      players with profile photos, a Pun King, a karaoke result, a Match Draw
      winner, and at least one blow-ball photo — confirm the song references
      real names/teams/moments and isn't generic.
- [ ] Confirm all three genres (rap/rock/folk) produce noticeably different
      songs — run it a few times or temporarily force each genre to check.
- [ ] Confirm the generated audio is close to 60 seconds and the video
      recording length matches it (no silent tail or early cutoff).
- [ ] Confirm the photo montage includes profile pics AND round photos (not
      just blow-ball), in a sensible order, with no duplicate images.
- [ ] Confirm the offline/failure fallback (`FALLBACK_SONG`) still plays
      cleanly if the ElevenLabs call fails or times out.
- [ ] Check the ElevenLabs API key usage/cost — Music API generation consumes
      credits per call (composition-plan drafting does not), so avoid
      regenerating on every test; cache/log responses while iterating.
