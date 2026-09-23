# Foul Play — Game Summary

## What Is It?

Foul Play is a live, host-led multiplayer game show played in a room. One person runs the game on a laptop or TV (the host screen), and everyone else joins on their phones. The theme is World Cup football. It runs through a sequence of rounds — quizzes, physical challenges, creative tasks, and hidden social games — building to a final score reveal. A full game takes roughly 90 minutes to 2 hours.

---

## Technology

| Layer | What's Used |
|---|---|
| **Realtime sync** | Firebase Realtime Database (project: `soccer-quiz-game-cf039`, EU West region) |
| **Frontend** | Vanilla HTML/CSS/JavaScript — no framework |
| **Voice & commentary** | ElevenLabs text-to-speech API (dynamic narration, score commentary, pun reads) |
| **Face swap** | fal.ai API (used in the Punned It round) |
| **Fonts** | Bebas Neue, Barlow, Oswald (Google Fonts) |
| **QR codes** | qrserver.com API (auto-generates join QR on host screen) |
| **Storage** | Firebase Storage (player photos, blowball photos, commentary recordings) |

### Files

- **`host-complete_42.html`** — The host screen. Runs on a laptop/TV. Controls all game state, plays audio, advances rounds.
- **`player-complete_27.html`** — The player screen. Loaded on every phone. Reacts to Firebase state changes to show the right UI at the right time.

All game state lives in Firebase under `games/{gameCode}/`. The host writes state, players read and respond to it. There is no server-side logic — everything runs in the browser.

---

## How Players Join

1. The host screen shows a QR code (draggable, resizable) in the corner at all times.
2. Players scan it or type the 4-character game code at the player URL.
3. They enter their name, take a selfie (used throughout the game), and pick a team.
4. They wait on a lobby screen until the host starts.

Players who leave and come back see a "Welcome Back" rejoin screen — their ID, name, and score are stored in `localStorage`.

**Spectator mode** is also available via `?spectator` in the URL — watch-only, no interaction.

---

## Team Setup

Before the game starts, the host picks two World Cup nations from a flag/country picker. Each team gets its flag, name, and colour. A "Today's Match" card is shown. Players join as Home or Away. The two team names are immediately sent to ElevenLabs to pre-generate the intro commentary — so by the time the host clicks Confirm, the audio is already cached.

---

## Game Flow

```
Round 1 (Quiz)
  → Bonus: Karaoke
  → Scores Review
Round 2 (Punned It)
  → Pun Review / Pun King reveal
  → Scores Review
Team Talk
Round 3 (Interview)
  → Scores Review
Match Draw  (4+ players only)
  → Scores Review
Commentary Round
Toilet Paper / Bog Rolling
  → Sabotage assignments happen here
Goal Post Glory
Blow Ball
  → Caption Contest
Extra Time
  → Sabotage Reveals
  → Final Score & Victory Screen
```

Each round transition plays a short intro music sting before the round's voice explanation. All audio is managed through a central pool so the pause button always works.

---

## The Rounds

### Round 1 — Sing When You're Beginning
A multiple-choice quiz. Questions are based on World Cup anthem lyrics and football knowledge. Players answer on their phones; the host sees responses in real time and reveals answers one at a time. Points are tracked per team.

### Bonus — Karaoke
One team at a time performs a karaoke song. The host judges how they got on. Scores added.

### Round 2 — Punned It
Players have 60 seconds to turn a footballer's name into a pun on a given theme (Birds, Food, Movies, Famous People, etc.). Both teams get the **same theme**. Submissions are reviewed one by one with ElevenLabs reading each pun aloud. The host Accepts or Rejects each. The player with the most accepted puns is crowned **The Pun King** on a reveal screen.

### Team Talk
A rapid-fire word-guessing game. One team's "scorer" watches on their phone and presses Correct or Skip as their teammates describe words. 120 seconds per team. Words unlock progressively: first 15 seconds football only, then sports, then anything. Words carry difficulty-based points (1–10). ElevenLabs reads out the scores afterwards.

### Round 3 — Interview Round
Players are given a journalist question (e.g. *"What would you say is your biggest strength?"*) and must pick a funny answer from a randomised set of options on their phone. Once everyone has submitted, the host reveals the answers one at a time. Players vote for their favourite. The winning answer is read aloud by ElevenLabs. The round auto-advances through all questions once votes are in — no "Next" button needed.

**Questions:**
1. The team looked tired. What did you give them at half time?
2. What are you most concerned about in the next game?
3. What are you most excited about?
4. What would you say is your biggest strength?

### Match Draw *(4+ players only)*
A Telestrations-style chain drawing game. Each player gets a subject (one random player gets a harder prompt), draws it in 45 seconds, passes it along, and the next player guesses from the drawing. Chains are revealed and scored at the end. Easy subjects are football-themed; hard subjects are wildly off-topic (e.g. *"Jean Claude Van Damme"*, *"Ancient Mayan temple"*).

### Commentary Round
A random player from each team volunteers as commentator. They watch a World Cup video clip on their own phone and provide live commentary via microphone. The recording is played back for everyone to hear and enjoy.

### Bog Rolling / Toilet Paper Rounds
The physical section of the game. Players are given a roll of toilet paper each.

- **Bog Rolling** — the main physical challenge with the toilet paper.
- **Goal Post Glory** — teams build the tallest goal posts they can from toilet paper. Scored out of 11 by the host.
- **Blow Ball** — players blow a ball of paper across a surface. The team who scores first gets +17 bonus points. The referee (Player 1) photographs the action and scores each team out of 23 on a sliding scale.

### Caption Contest
Five rounds, each with a different photo prompt:

| # | Task |
|---|---|
| 1 | Write the Sky Sports breaking news ticker |
| 2 | Write the Instagram caption |
| 3 | Write the crowd chant |
| 4 | Write the newspaper headline |
| 5 | Draw something |

Players submit on their phones. The host reads them out. Everyone votes for their favourite. Winner gets points.

### Extra Time — Sabotage Reveals
This is the hidden social game. At the start of the bog rolling section, each player was secretly assigned a **sabotage challenge** from the Quick Pass set. They've been completing tasks in secret throughout the physical rounds. Now the host reveals them one by one, with a dramatic audio sting and toilet-roll-noise effect for each reveal. Players declare whether they completed their task and the host judges.

**Sabotage Challenges include:**
- *Clean Sheet* — collect loose pieces in your pockets undetected
- *On The Bench* — hide pieces in a secret location
- *Yellow Card* — wear pieces tucked under clothing
- *Quick Pass* — give someone as many individual pieces as possible; 1 point per piece they still have at the end
- *Extra Time* — wrap a limb like a cast
- *Hat Trick* — make and wear a toilet paper hat
- *Take a Dive* — convince someone they pushed you (0 or 20 points)
- *Golden Boot* — kick someone (auto-award)

---

## Scoring

Points are tracked per player and summed by team. The scoreboard is always visible on the host screen with team flags and running totals. After most rounds, a Scores Review plays with:
1. A generic "colour commentary" audio reaction
2. An ElevenLabs-generated line contextual to the current score gap
3. A contextual audio reaction (struggling / close / leading)

The final Victory Screen shows team totals, a photo album of all the blowball/action photos taken during the game, and a fanfare.

---

## Audio Design

Almost every moment in the game has accompanying audio. Key pieces:

- **Round intro music stings** — play before each round's voice explainer
- **ElevenLabs dynamic commentary** — generated fresh each game using team names and scores
- **Pre-recorded voice clips** — pun reactions (accept/reject), scores reactions, explainers for each round
- **Sound effects** — final whistle, toilet roll noise, victory fanfare, dings
- **Countdown music** — quiet 15-second backing track during timed phases

All audio goes through a central reference pool (`window._audioRefs`) so the pause button reliably stops everything.

---

## The Host Experience

The host never touches their phone. Everything runs from one browser tab on a laptop or plugged into a TV. They:

- Pick teams from a flag picker
- Start rounds with a single button
- Reveal answers, accept/reject puns, judge physical tasks
- See live player submissions appear on screen
- Have a pause button that freezes all audio across the game

The QR code is always visible in the corner so latecomers can join at any point.

---

## The Player Experience

Players interact entirely through their phone browser — no app install required. At any given moment a player might be:

- Tapping a multiple-choice answer
- Typing a pun
- Drawing on a canvas
- Watching a video clip and recording their voice
- Using their rear camera to take a photo
- Sneaking toilet paper onto someone without them noticing

The phone UI is fullscreen, dark-themed, and designed for quick glances — large buttons, high contrast, minimal text.
