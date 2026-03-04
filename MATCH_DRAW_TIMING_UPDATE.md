# MATCH DRAW TIMING UPDATE

## ✅ CHANGE MADE

**Subject Viewing Time:** 5 seconds → **15 seconds**

---

## 📝 UPDATED GAME FLOW

### Before:
```
Show subject → 5 second countdown → Draw for 30 seconds
```

### After:
```
Show subject → 15 second countdown → Draw for 30 seconds
```

---

## 🎯 WHY THIS CHANGE?

**Problem:** 5 seconds is too short to:
- Read the subject
- Understand what to draw
- Plan the drawing

**Solution:** 15 seconds gives players:
- Time to read and process
- Time to think about approach
- Less rushed feeling
- Better quality drawings

---

## 🔧 WHAT WAS UPDATED

### 1. Game Rules Documentation
**File:** `COMPLETE_GAME_IMPLEMENTATION.md`

Changed from:
```
- 5 seconds to view subject
```

To:
```
- 15 seconds to view subject
```

---

### 2. Code Implementation
**File:** `COMPLETE_GAME_IMPLEMENTATION.md`

Changed countdown call from:
```javascript
showCountdown(5, () => {
  startDrawingPhase(roundNumber);
});
```

To:
```javascript
showCountdown(15, () => {
  startDrawingPhase(roundNumber);
});
```

---

### 3. Audio File Reference
**File:** `COMPLETE_GAME_IMPLEMENTATION.md`

Changed from:
```javascript
const countdownAudio = new Audio('countdown_5sec.mp3?v=2');
```

To:
```javascript
const countdownAudio = new Audio('countdown_15sec.mp3?v=2');
```

---

### 4. Player Display Text
**File:** `COMPLETE_GAME_IMPLEMENTATION.md`

Changed from:
```
Memorize this - you'll draw it in 5 seconds
```

To:
```
Memorize this - you'll draw it in 15 seconds
```

---

### 5. Audio Files List
**File:** `COMPLETE_AUDIO_VIDEO_FILES_LIST.md`

**OLD:**
- **countdown_5sec.mp3** - 5-second countdown (5, 4, 3, 2, 1, GO!)

**NEW:**
- **countdown_15sec.mp3** - 15-second countdown (15, 14, 13... 3, 2, 1, GO!)

---

## 🎙️ NEW AUDIO FILE NEEDED

### countdown_15sec.mp3

**Content:** Full 15-second countdown with beats

**Script Options:**

**Option 1: Full Count**
```
15... 14... 13... 12... 11... 10... 9... 8... 7... 6... 5... 4... 3... 2... 1... GO!
```

**Option 2: Strategic Count (Recommended)**
```
[Beat]
15 seconds to memorize
[Beat at 10]
10 seconds
[Beats at 5, 4, 3, 2, 1]
5... 4... 3... 2... 1... GO!
```

**Option 3: Music with Call-outs**
```
[Upbeat music playing]
[At 10 seconds] "10 seconds left"
[At 5 seconds] "5... 4... 3... 2... 1... GO!"
```

**Duration:** 15 seconds exactly
**Voice:** Host (Clyde) or sound effects with music
**Priority:** HIGH

---

## 🎯 COMPLETE MATCH DRAW TIMING

### Phase Breakdown:

1. **Subject View:** 15 seconds (NEW - was 5)
   - Players see their subject
   - Time to read and understand
   - Time to plan approach

2. **Drawing:** 30 seconds (unchanged)
   - Canvas appears
   - Players draw their subject
   - Music plays in background

3. **Swap:** 2-3 seconds (unchanged)
   - Transition animation
   - "Time to swap" audio

4. **Guessing:** 15 seconds (unchanged)
   - Players see previous drawing
   - Type their guess
   - Submit

5. **Repeat** until full rotation complete

---

## 📊 TOTAL ROUND TIME IMPACT

### Per Round (4 players example):

**Before (5 sec view):**
- View: 5 seconds
- Draw: 30 seconds
- Swap: 3 seconds
- Guess: 15 seconds
- Swap: 3 seconds
**Total per cycle:** 56 seconds × 4 rounds = **224 seconds (3.7 minutes)**

**After (15 sec view):**
- View: 15 seconds
- Draw: 30 seconds
- Swap: 3 seconds
- Guess: 15 seconds
- Swap: 3 seconds
**Total per cycle:** 66 seconds × 4 rounds = **264 seconds (4.4 minutes)**

**Difference:** +40 seconds total (+0.7 minutes)

**Verdict:** Minor increase, well worth it for better gameplay quality

---

## ✅ IMPLEMENTATION CHECKLIST

When implementing Match Draw, make sure to:

- [ ] Use 15-second countdown (not 5)
- [ ] Create countdown_15sec.mp3 audio file
- [ ] Update showCountdown() call with 15
- [ ] Update player message to say "15 seconds"
- [ ] Test timing feels right
- [ ] Adjust if needed after playtesting

---

## 🎮 GAMEPLAY NOTES

**15 seconds is enough time to:**
- ✅ Read complex subjects ("Traditional Japanese tea ceremony")
- ✅ Process what needs to be drawn
- ✅ Plan composition
- ✅ Not feel rushed

**But not so long that:**
- ❌ Players get bored waiting
- ❌ Game drags
- ❌ Tension is lost

**Perfect balance for:**
- Party game pacing
- Casual players
- Complex subjects
- Drawing variety

---

## 🔄 FUTURE ADJUSTMENTS

After playtesting, you might want to:

**If too long:**
- Reduce to 12 seconds
- Keep 15 for hard subjects only

**If too short:**
- Increase to 20 seconds
- Add "Need more time?" button

**Dynamic timing:**
- 10 seconds for easy subjects
- 15 seconds for hard subjects
- Players choose

---

## 📝 SUMMARY

✅ **Changed:** Subject viewing time from 5 to 15 seconds
✅ **Updated:** All documentation and code
✅ **New audio needed:** countdown_15sec.mp3
✅ **Impact:** +40 seconds total round time
✅ **Benefit:** Better gameplay, less rushed, higher quality

**Status:** Ready for implementation

---

END OF MATCH DRAW TIMING UPDATE
