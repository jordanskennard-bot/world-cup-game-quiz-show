# MATCH DRAW - ALTERNATING MUSIC TRACKS

## 🎵 FEATURE ADDED

**Two Music Tracks:** Instead of one repeating music file, the game now alternates between two different tracks to add variety and keep players engaged.

---

## 📝 HOW IT WORKS

### Music Files:
1. **matchdraw_music_30sec_1.mp3** - Plays on ODD rounds (1, 3, 5, 7...)
2. **matchdraw_music_30sec_2.mp3** - Plays on EVEN rounds (2, 4, 6, 8...)

### Example with 4 Players (4 rounds total):

```
Round 1 (Draw) → Music Track 1 plays
Round 2 (Draw) → Music Track 2 plays
Round 3 (Draw) → Music Track 1 plays
Round 4 (Draw) → Music Track 2 plays
```

---

## 🔧 IMPLEMENTATION

### Code Logic:

```javascript
// In startDrawingPhase() function
gameRef.child('matchDraw/currentRound').once('value', (snapshot) => {
  const currentRound = snapshot.val() || 1;
  
  // Alternate between two music files
  const musicFile = currentRound % 2 === 1 
    ? 'matchdraw_music_30sec_1.mp3' 
    : 'matchdraw_music_30sec_2.mp3';
  
  const musicAudio = new Audio(`${musicFile}?v=2`);
  musicAudio.loop = true;
  musicAudio.volume = 0.4;
  musicAudio.play().catch(e => console.log('Music failed:', e));
  window.matchDrawMusic = musicAudio;
});
```

### How It Works:
- `currentRound % 2 === 1` checks if round is odd (1, 3, 5...)
- Odd rounds → Track 1
- Even rounds → Track 2
- Both tracks loop during the 30-second drawing phase

---

## 🎨 MUSIC SELECTION GUIDELINES

### Track 1 (Odd Rounds):
**Suggested Style:**
- Upbeat and energetic
- Mid-tempo (120-130 BPM)
- Playful instruments (piano, xylophone, synth)
- Encouraging vibe
- Clean loop point at 30 seconds

**Example mood:** "Let's get creative!" energy

### Track 2 (Even Rounds):
**Suggested Style:**
- Also upbeat but different feel
- Slightly different tempo (110-125 BPM)
- Different instrumentation (guitar, marimba, bells)
- Fun and quirky
- Clean loop point at 30 seconds

**Example mood:** "Keep the creativity flowing!" energy

### Important Requirements:
✅ Both must be **exactly 30 seconds**
✅ Both must **loop seamlessly** (no gap/click when restarting)
✅ Both should be **similar volume levels**
✅ Both should be **upbeat and positive**
✅ But **different enough** to provide variety

---

## 🎯 WHY ALTERNATING MUSIC?

### Benefits:
1. **Reduces Repetition:** Players don't hear the same music 4+ times
2. **Maintains Energy:** Fresh music keeps engagement high
3. **Variety:** Makes longer games more enjoyable
4. **Subtle Change:** Players notice the difference subconsciously
5. **Professional Touch:** Shows attention to detail

### Player Experience:
```
Round 1: "Oh, fun music!"
Round 2: "New music! Nice change!"
Round 3: "Ah, the first track again - but I like it!"
Round 4: "Back to the second one - keeps it fresh!"
```

---

## 📊 FILE STATUS

### Audio Files Needed:

**Before this change:**
- ❌ matchdraw_music_30sec.mp3 (single file)

**After this change:**
- ✅ matchdraw_music_30sec_1.mp3 (Track 1 for odd rounds)
- ✅ matchdraw_music_30sec_2.mp3 (Track 2 for even rounds)

**You already have both files!** ✅

---

## 🎵 PRODUCTION TIPS

### If Creating from Scratch:

**Option 1: Use Royalty-Free Music**
- incompetech.com (Kevin MacLeod)
- bensound.com
- freemusicarchive.org
- Search for "upbeat game music"

**Option 2: Use AI Music Generation**
- Suno.ai
- Udio.com
- Mubert.com
- Generate 30-second upbeat game music

**Option 3: Use Stock Music**
- AudioJungle ($5-15 per track)
- Epidemic Sound (subscription)
- Artlist (subscription)

### Editing Tips:
1. **Loop Point:** Make sure track ends where it can smoothly restart
2. **Fade:** Add tiny fade in/out at loop point if needed
3. **Volume:** Normalize both tracks to same perceived loudness
4. **Format:** Export as MP3, 128kbps or higher
5. **Test:** Play both and make sure they feel like they belong together

---

## ✅ TESTING CHECKLIST

When testing Match Draw:

- [ ] Round 1 plays Track 1
- [ ] Round 2 plays Track 2
- [ ] Round 3 plays Track 1 again
- [ ] Round 4 plays Track 2 again
- [ ] Both tracks loop smoothly (no gap/click)
- [ ] Volume levels are consistent
- [ ] Tracks complement each other
- [ ] Music stops when drawing phase ends
- [ ] No overlap between rounds

---

## 🔄 EXTENSION IDEAS

### Future Enhancements:

**Option 1: Pool of Tracks**
Instead of just 2, use 3-5 tracks and randomize:
```javascript
const tracks = [
  'matchdraw_music_1.mp3',
  'matchdraw_music_2.mp3',
  'matchdraw_music_3.mp3'
];
const randomTrack = tracks[Math.floor(Math.random() * tracks.length)];
```

**Option 2: Player Count Based**
Different music for different player counts:
```javascript
const trackIndex = Math.min(playerCount - 3, 4); // Max 4 tracks
const musicFile = `matchdraw_music_${trackIndex}.mp3`;
```

**Option 3: Tempo Increase**
Speed up music slightly each round:
```javascript
musicAudio.playbackRate = 1.0 + (currentRound * 0.05); // 5% faster each round
```

---

## 📝 SUMMARY

✅ **Added:** Alternating music tracks for Match Draw drawing phase
✅ **Files needed:** 2 (matchdraw_music_30sec_1.mp3 and _2.mp3)
✅ **Status:** Already have both files
✅ **Logic:** Odd rounds = Track 1, Even rounds = Track 2
✅ **Benefit:** Reduces repetition, maintains energy
✅ **Implementation:** Simple modulo check in code

**Ready to use!** Just make sure both files are uploaded to GitHub. 🎵✨

---

END OF ALTERNATING MUSIC FEATURE
