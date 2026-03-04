# FOUL PLAY - IMPLEMENTATION STATUS & TASKS FOR CLAUDE CODE
## Current State vs Required Changes

---

## 📊 CURRENT FILE STATUS

### Host File: `host-complete_42.html`
**Version:** 8.0
**Lines:** 3,697
**Description:** Full game flow with Bonus Round, Match Draw, and Victory Screen

### Player File: `player-complete_27.html`
**Version:** 7.0
**Lines:** 2,785
**Description:** Full game with Bonus Round, Match Draw, and Victory Screen

---

## ✅ WHAT'S ALREADY IMPLEMENTED

### Phase 0 Fixes (Partially Complete)
✅ **Fix 1:** "That's right John" → "Thanks Clyde" (DONE)
❌ **Fix 2:** Preload ALL Round 1 audio files (NOT DONE)
❌ **Fix 3:** Change pun timer from 60 to 30 seconds (PARTIALLY DONE - inconsistent)
✅ **Fix 4:** ElevenLabs API (appears to be working)

### Phase 1: Bonus Round
✅ Bonus offer screen (implemented)
✅ Karaoke functionality (implemented)
✅ Referee judging (implemented)
✅ Points award/deduct (implemented)

### Phase 2: Match Draw
✅ Round introduction (implemented)
✅ Subject assignment (implemented)
✅ Drawing phase (implemented)
✅ Guessing phase (appears implemented)
✅ Reveal and scoring (implemented)
✅ Music alternating (code present for two tracks)

### Phase 6: Victory Screen
✅ Winner announcement (implemented)
✅ MVP calculation (implemented)
✅ Final scores display (implemented)

### Additional Features Not Requested Yet
✅ Test buttons for debugging
✅ Firebase structure
✅ Basic game flow (Round 1, Round 2, Scores)

---

## ❌ WHAT'S MISSING - CRITICAL FIXES NEEDED

### 1. Round 1 Audio Preloading (HIGH PRIORITY)
**Status:** NOT IMPLEMENTED
**Issue:** Audio files load slowly, causing delays
**Required:** Preload all 8 R1 audio files when first player joins

**Implementation Needed:**
```javascript
// In host-complete.html, find where first player joins (around line 1500)
// Add after existing preloading code:

console.log('🎵 Preloading all Round 1 Q&A audio (8 files)');
window.r1AudioPreload = {};

for (let i = 1; i <= 4; i++) {
  // Questions
  const qAudio = new Audio(`R1_Q${i}_Q.mp3?v=2`);
  qAudio.preload = 'auto';
  qAudio.volume = 0.6;
  qAudio.load();
  window.r1AudioPreload[`q${i}`] = qAudio;
  
  // Answers
  const aAudio = new Audio(`R1_Q${i}_A.mp3?v=2`);
  aAudio.preload = 'auto';
  aAudio.volume = 0.6;
  aAudio.load();
  window.r1AudioPreload[`a${i}`] = aAudio;
}
```

Then update `loadQuestion()` and `revealAnswer()` functions to use preloaded audio:
```javascript
// In loadQuestion (around line 1925)
let questionAudio;
if (window.r1AudioPreload && window.r1AudioPreload[`q${questionNumber}`]) {
  questionAudio = window.r1AudioPreload[`q${questionNumber}`];
} else {
  questionAudio = new Audio(questionAudioFile);
  questionAudio.volume = 0.6;
}
```

---

### 2. Pun Timer Inconsistency (MEDIUM PRIORITY)
**Status:** PARTIALLY FIXED
**Issue:** Timer declared as 60 but set to 30 inconsistently

**Current State:**
- Line 2257: `let round2TimeLeft = 60;` ❌
- Line 2363: `round2TimeLeft = 30;` ✅

**Fix Needed:**
Change line 2257 from:
```javascript
let round2TimeLeft = 60;
```
To:
```javascript
let round2TimeLeft = 30;
```

**Also check for any other references to 60 seconds in Round 2**

---

### 3. Team Captain Feature (MEDIUM PRIORITY - NEW FEATURE)
**Status:** NOT IMPLEMENTED
**Requirement:** Players 1 & 2 should be marked as captains, players 3+ choose which captain to join

**Implementation Needed in `host-complete.html`:**

Find player join logic (around line 1475) and update:
```javascript
gameRef.child('players').on('child_added', (snapshot) => {
  const playerId = snapshot.key;
  const playerData = snapshot.val();
  
  // Count current players
  const currentPlayerCount = Object.keys(players).length;
  
  if (currentPlayerCount === 0) {
    // First player - Team 1 Captain
    gameRef.child(`players/${playerId}`).update({
      team: 1,
      isCaptain: true
    });
  } else if (currentPlayerCount === 1) {
    // Second player - Team 2 Captain
    gameRef.child(`players/${playerId}`).update({
      team: 2,
      isCaptain: true
    });
  } else {
    // 3+ players - no team yet, will choose
    gameRef.child(`players/${playerId}`).update({
      team: null,
      isCaptain: false
    });
  }
  
  players[playerId] = { ...playerData, id: playerId };
  showLobbyPlayers();
});
```

Update lobby display to show captain badges:
```javascript
// In showLobbyPlayers() function
Object.values(players).forEach((player) => {
  const isCaptain = player.isCaptain || false;
  const captainBadge = isCaptain ? '⚽ CAPTAIN' : '';
  // Add visual badge for captains
});
```

**Implementation Needed in `player-complete.html`:**

Add team selection screen for players 3+:
```javascript
function showTeamSelection() {
  gameRef.child('players').once('value', (snapshot) => {
    const allPlayers = snapshot.val();
    const captains = Object.entries(allPlayers)
      .filter(([id, player]) => player.isCaptain)
      .sort((a, b) => a[1].team - b[1].team);
    
    if (captains.length < 2) return;
    
    const team1Captain = captains[0][1];
    const team2Captain = captains[1][1];
    
    // Show selection UI with captain names
    // Buttons to join Team 1 or Team 2
  });
}
```

---

## 🎯 NEW FEATURES TO ADD

### Phase 3: Commentary Round (FUTURE - NOT URGENT)
**Status:** NOT IMPLEMENTED
**Complexity:** HIGH (requires microphone recording)
**Defer until:** After core game is working

### Phase 4: Toilet Paper Rounds (FUTURE - NOT URGENT)
**Status:** NOT IMPLEMENTED
**Complexity:** HIGH (requires camera/photo upload)
**Defer until:** After core game is working

### Phase 5: Interview Round Integration (MEDIUM PRIORITY)
**Status:** Already built, needs integration
**Action:** Hook existing interview round into game flow after Match Draw

---

## 📁 AUDIO FILES STATUS

### Files Already on GitHub (38 files)
✅ All lobby/intro music
✅ All Round 1 Q&A (8 files)
✅ All score reactions
✅ Round 2 intro & music
✅ Karaoke video

### Critical Missing Files (2 files)
❌ **puns_review_intro.mp3** - "Let's see what we've got!"
❌ **offside_caught.mp3** - Whistle + "Offside!"

### Phase 1 Needed (4 files)
❌ **bonus_alert.mp3** - Alert sound
❌ **bonus_explainer.mp3** - Challenge explanation
❌ **bonus_setup.mp3** - "They'll need to sing..."
❌ **bonus_judging.mp3** - "How did they get on?"

### Phase 2 Needed (24 files)
❌ **matchdraw_explainer.mp3**
❌ **countdown_15sec.mp3** (was 5sec, changed to 15sec)
❌ **matchdraw_draw.mp3**
❌ **matchdraw_music_30sec_1.mp3** (odd rounds)
❌ **matchdraw_music_30sec_2.mp3** (even rounds)
❌ **matchdraw_swap.mp3**
❌ **matchdraw_reveal_1.mp3** through **matchdraw_reveal_10.mp3** (10 files)
❌ **matchdraw_subject_reveal_1.mp3** through **matchdraw_subject_reveal_10.mp3** (10 files)

### Phase 6 Needed (2 files)
❌ **final_whistle.mp3**
❌ **victory_fanfare.mp3**

**Total New Audio Files Needed: 32 files**

---

## 🎵 SPECIAL AUDIO FILE NOTES

### 1. Toilet Paper Alert (Dual Audio)
- **Toilet_paper_alert.mp3** (capital T) - Sound effect plays first
- **toilet_paper_alert.mp3** (lowercase t) - Voice plays second

### 2. Bog Rolling Music (Loops)
- **bog_rolling_60sec.mp3** - Actually 30 seconds, loops twice
- Set `loop = true` in code

### 3. Match Draw Music (Alternates)
- **matchdraw_music_30sec_1.mp3** - Odd rounds (1, 3, 5...)
- **matchdraw_music_30sec_2.mp3** - Even rounds (2, 4, 6...)
- Code already implements alternating logic

### 4. Countdown Changed
- Was: **countdown_5sec.mp3** (5 seconds)
- Now: **countdown_15sec.mp3** (15 seconds)
- Player message changed to "15 seconds"

---

## 🔧 IMMEDIATE TASKS FOR CLAUDE CODE

### Priority 1: Critical Fixes (DO FIRST)

**Task 1.1: Add Round 1 Audio Preloading**
- File: `host-complete.html`
- Location: Around line 1500 (where first player joins)
- Action: Add preloading code for 8 audio files
- Update: `loadQuestion()` and `revealAnswer()` functions

**Task 1.2: Fix Pun Timer Declaration**
- File: `host-complete.html`
- Location: Line 2257
- Action: Change `let round2TimeLeft = 60;` to `30`
- Verify: No other 60-second references in Round 2

**Task 1.3: Check Match Draw Timing**
- File: `host-complete.html`
- Location: Match Draw implementation (around line 3175+)
- Action: Verify countdown is 15 seconds not 5 seconds
- Action: Verify audio file reference is `countdown_15sec.mp3`

---

### Priority 2: Team Captain Feature (DO SECOND)

**Task 2.1: Add Captain Assignment Logic**
- File: `host-complete.html`
- Location: Player join handler (around line 1475)
- Action: Assign `isCaptain: true` to first 2 players
- Action: Assign `isCaptain: false` and `team: null` to players 3+

**Task 2.2: Update Lobby Display**
- File: `host-complete.html`
- Location: `showLobbyPlayers()` function
- Action: Add captain badges (⚽ CAPTAIN) for players with `isCaptain: true`
- Action: Add gold styling for captain rows

**Task 2.3: Add Team Selection for Players 3+**
- File: `player-complete.html`
- Location: After player joins
- Action: Check if `team === null`
- Action: Show team selection screen with captain names
- Action: Add buttons to join Team 1 or Team 2

**Task 2.4: Update Country Selection Display**
- File: `player-complete.html`
- Location: `showCountrySelection()` function
- Action: Add captain badge at top for Players 1 & 2
- Action: Show "⚽ YOU ARE TEAM CAPTAIN ⚽"

---

### Priority 3: Audio File Integration (DO THIRD)

**Task 3.1: Add Missing Audio References**
- Files: Both `host-complete.html` and `player-complete.html`
- Action: Update audio file references where needed
- Check: All audio files are correctly named

**Task 3.2: Implement Bog Rolling Music Loop**
- File: `host-complete.html`
- Location: Bog rolling timer function (if implemented)
- Action: Set `musicAudio.loop = true` for 30-second file
- Action: Stop after 60 seconds

**Task 3.3: Implement Toilet Paper Alert Sequence**
- File: `host-complete.html`
- Location: Toilet paper alert function (if implemented)
- Action: Play `Toilet_paper_alert.mp3` first (sound effect)
- Action: Then play `toilet_paper_alert.mp3` (voice)

---

### Priority 4: Testing & Validation (DO FOURTH)

**Task 4.1: Test Round 1 Audio**
- Verify: All 8 files preload quickly
- Verify: Questions play instantly
- Verify: No delays or timeouts

**Task 4.2: Test Pun Round Timer**
- Verify: Timer counts from 30 to 0
- Verify: No references to 60 seconds
- Verify: Music stops at 0

**Task 4.3: Test Team Captain Flow**
- Verify: Player 1 sees captain badge
- Verify: Player 2 sees captain badge
- Verify: Player 3 sees team selection
- Verify: Can choose either team
- Verify: Game continues normally

**Task 4.4: Test Bonus Round**
- Verify: Appears after Round 1
- Verify: Audio plays correctly
- Verify: Fastest player selection works
- Verify: Karaoke video plays
- Verify: Referee judging works
- Verify: Points awarded/deducted correctly

**Task 4.5: Test Match Draw**
- Verify: Only plays with 4+ players
- Verify: 15-second subject viewing
- Verify: Drawing canvas works
- Verify: Music alternates between tracks
- Verify: Guessing works
- Verify: Reveal shows full chain
- Verify: Referee scoring works

**Task 4.6: Test Victory Screen**
- Verify: Shows correct winner
- Verify: Calculates MVP correctly
- Verify: Displays all scores
- Verify: Looks polished

---

## 📋 FILE CHANGES SUMMARY

### host-complete.html Changes Needed:
1. ✅ Line 2257: Change `round2TimeLeft = 60` to `30`
2. ➕ Around line 1500: Add Round 1 audio preloading (8 files)
3. ✏️ Around line 1925: Update `loadQuestion()` to use preloaded audio
4. ✏️ Around line 2000: Update `revealAnswer()` to use preloaded audio
5. ➕ Around line 1475: Add captain assignment in player join handler
6. ✏️ Update `showLobbyPlayers()`: Add captain badges
7. ✅ Verify Match Draw uses 15-second countdown
8. ✅ Verify Match Draw references `countdown_15sec.mp3`
9. ✅ Verify music alternating works (two tracks)

### player-complete.html Changes Needed:
1. ➕ Add team selection screen for players 3+
2. ➕ Add `showTeamSelection()` function
3. ➕ Add `joinTeam(teamNumber)` function
4. ✏️ Update `showCountrySelection()`: Add captain badge for P1 & P2
5. ✅ Verify Bonus Round screens work
6. ✅ Verify Match Draw player screens work

---

## 🎯 IMPLEMENTATION ORDER

### Week 1: Core Fixes (Most Important)
1. Add Round 1 audio preloading
2. Fix pun timer inconsistency
3. Test and verify fixes work

### Week 2: Team Captain Feature
1. Add captain assignment logic
2. Add captain badges to UI
3. Add team selection for players 3+
4. Test with 2, 3, 4, 5+ players

### Week 3: Audio File Creation
1. Create 2 critical missing files
2. Create 4 Bonus Round files
3. Test Bonus Round end-to-end

### Week 4: Match Draw Polish
1. Create 24 Match Draw audio files
2. Test Match Draw end-to-end
3. Verify music alternating works

### Week 5: Victory Screen Polish
1. Create 2 Victory Screen files
2. Test full game flow
3. Bug fixes and polish

---

## 🚀 READY TO START

**Give these instructions to Claude Code:**

1. **Start with Priority 1 (Critical Fixes)**
   - Add audio preloading
   - Fix timer inconsistency
   - Test thoroughly

2. **Then Priority 2 (Team Captains)**
   - Implement captain logic
   - Add UI badges
   - Add team selection
   - Test with multiple players

3. **Then Priority 3 & 4 (Audio & Testing)**
   - Update audio references
   - Test everything works
   - Create list of needed audio files

**Current files are at Version 8.0 (host) and 7.0 (player)**
**Target: Version 9.0 with all fixes and captain feature**

---

## 💡 NOTES FOR CLAUDE CODE

### Testing Tips:
- Use test buttons at bottom of host screen
- Test with real phones, not just desktop
- Check Firebase console for data
- Check browser console for errors
- Test with 2, 3, 4, 5+ players

### Audio File Creation:
- Can defer audio creation until code works
- Use ElevenLabs for voice files
- Use free sound effects for alerts
- Use royalty-free music for jingles

### Known Working Features:
- Round 1 quiz works
- Round 2 puns work
- Bonus Round implemented
- Match Draw implemented
- Victory Screen implemented
- Just need fixes and polish!

---

## ✅ SUCCESS CRITERIA

Game is ready to launch when:
- [ ] Round 1 audio loads instantly
- [ ] Pun timer consistently shows 30 seconds
- [ ] Captain badges show for Players 1 & 2
- [ ] Players 3+ can choose teams
- [ ] Bonus Round plays without errors
- [ ] Match Draw works with 4+ players
- [ ] Victory Screen displays correctly
- [ ] All critical audio files created
- [ ] Full game tested with 5+ players
- [ ] No console errors
- [ ] Smooth flow from start to finish

---

END OF IMPLEMENTATION STATUS
READY FOR CLAUDE CODE TO BEGIN! 🎮⚽✨
