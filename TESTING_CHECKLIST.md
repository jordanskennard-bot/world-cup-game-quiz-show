# GITHUB UPLOAD & TESTING CHECKLIST

## 📤 FILES TO UPLOAD TO GITHUB

### ✅ MUST UPLOAD (CRITICAL)
1. **host-complete.html** (NEW VERSION)
   - Location: Download from outputs
   - Fixes: Round 2 duplication, timer issues, commentary crash
   - Upload to: Root of repository (replace existing)

2. **player-complete.html** (CURRENT VERSION)  
   - Location: Download from outputs
   - Fixes: Question order swapped (Q1 and Q2)
   - Upload to: Root of repository (replace existing)

---

## 🎵 AUDIO FILES STATUS

### Already on GitHub ✅
- intro_music.mp3
- intro_2.mp3  
- round_1_intro.mp3
- R1_Q1_Q.mp3 through R1_Q4_A.mp3 (8 files)
- Commentary_1.mp3
- close_score_reaction_1.mp3
- slight_lead_reaction_1.mp3
- comfortable_lead_reaction_1.mp3
- dominant_lead_reaction_1.mp3
- struggling_reaction_1.mp3
- round_2_intro.mp3
- round_2_music.mp3

### Still Missing 🔴
- puns_review_intro.mp3 (for "What have we got?")
- offside_caught.mp3 (whistle sound)

**Note:** Game will work without these two files - features just won't have audio

---

## 🧪 TESTING PROTOCOL

### Test 1: Lobby & Team Selection
- [ ] Open host page
- [ ] QR code appears
- [ ] Join with 2 players on phones
- [ ] intro_music.mp3 plays (might be slow first time)
- [ ] Click "Select Teams & Start"
- [ ] intro_2.mp3 plays
- [ ] Both players select teams
- [ ] ElevenLabs voice plays: "That's right John..."
- [ ] NO ERRORS in console

**Expected Console Logs:**
```
🎵 First player connected - music ready to play on interaction
🎵 Preloading intro_2.mp3 for faster playback
🎵 Playing intro_2.mp3 on host
✅ Voice generated successfully
🔊 Playing intro voice
```

---

### Test 2: Round 1
- [ ] Round 1 explainer appears
- [ ] round_1_intro.mp3 plays ONCE (not twice!)
- [ ] First player clicks "Start Round 1"
- [ ] Questions appear in order:
  1. "To the King of Spain..." (Netherlands)
  2. "Mercenary swords..." (Italy)
  3. "No official lyrics..." (Spain)
  4. "NOT an official World Cup song..." 
- [ ] R1_Q1_Q.mp3 plays, then R1_Q1_A.mp3
- [ ] All 4 questions play
- [ ] NO "play() interrupted" errors

**Expected Console Logs:**
```
🎵 Playing round_1_intro.mp3
🔊 Playing round_1_intro
🎮 Player 1 started Round 1
🎵 Playing R1_Q1_Q.mp3?v=2
🔊 Question 1 audio playing
```

---

### Test 3: Scores Review (CRITICAL TEST)
- [ ] After Q4, scores screen appears
- [ ] Commentary_1.mp3 plays
- [ ] ElevenLabs commentary generates
- [ ] Reaction audio plays (based on score)
- [ ] Round 2 starts ONCE (not 4 times!)
- [ ] NO "Cannot set properties of null" error

**Expected Console Logs:**
```
📊 Showing scores review
🎵 Playing Commentary_1.mp3
🎙️ Generating ElevenLabs commentary: Germany took an early lead...
✅ Voice generated successfully
🎵 Playing struggling_reaction_1.mp3 (scores: 2 vs 0)
🔊 Playing scores reaction
✅ Reaction finished, moving to Round 2
🎯 Starting Round 2 - Showing explainer
```

**🚨 CRITICAL: Check console does NOT show:**
```
🎯 Starting Round 2 - Showing explainer  (appears 4 times) ❌
🎮 Starting Round 2 gameplay  (appears 4 times) ❌
```

---

### Test 4: Round 2 - Punned It (CRITICAL TEST)
- [ ] Round 2 explainer appears ONCE
- [ ] round_2_intro.mp3 plays ONCE
- [ ] Round 2 gameplay starts ONCE
- [ ] round_2_music.mp3 plays ONCE
- [ ] Timer counts down: 60, 59, 58...
- [ ] Timer STOPS at 0 (doesn't go negative!)
- [ ] Players can submit puns on their phones
- [ ] Host sees pun count increase
- [ ] "Next Round" button appears at 0

**Expected Console Logs:**
```
🎯 Starting Round 2 - Showing explainer
🎵 Playing round_2_intro.mp3
🔊 Playing round_2_intro
✅ Round 2 intro finished, starting round
🎮 Starting Round 2 gameplay
🎵 Playing round_2_music.mp3
🔊 Playing round_2_music
```

**🚨 Check Does NOT Show:**
```
⚠️ Timer already running, clearing old timer (if this appears, multiple timers started)
🎮 Starting Round 2 gameplay (appears multiple times) ❌
```

---

### Test 5: Player Screens
- [ ] **Scores Review:** Players see team scores after Round 1
- [ ] **Round 2:** Players see category and can type puns
- [ ] **Pun Submission:** Typing works, submit button works
- [ ] **Submitted Puns:** Each pun appears below with checkmark

**Player Phone Should Show:**
```
Round 1 Questions → Answer → Scores Screen → Round 2 Category → Text Input
```

---

## 🐛 KNOWN ISSUES (Still Need Fixing)

### Issues Fixed in Host ✅
- Round 2 starting 4 times
- Timer going negative
- Commentary div crash
- Audio playing multiple times

### Issues Still Remaining 🟡
1. **Audio Loading Slow** - Files may timeout on first load
   - Temp fix: Refresh page if audio doesn't play
   - Real fix: Host audio on faster CDN

2. **Pun Review Missing** - No way to review/accept/reject puns yet
   - Will add in next version

3. **First Player Controls** - First player should see "Review Puns" button
   - Will add in next version

4. **Question Order** - Only fixed in local files, need GitHub upload
   - Upload new player-complete.html to fix

---

## 📊 SUCCESS CRITERIA

### ✅ Test is SUCCESSFUL if:
1. Round 2 starts ONCE (not 4 times)
2. Timer stops at 0
3. No "Cannot set properties of null" errors
4. Questions in correct order (Netherlands first, Italy second)
5. Players can submit puns
6. Console logs are clean

### 🚨 Test FAILED if:
1. "Starting Round 2 gameplay" appears 4 times in console
2. Timer shows negative numbers
3. Any "Cannot set properties" errors
4. Questions in wrong order
5. Players can't type puns

---

## 🔄 IF TESTS FAIL

### If Round 2 Still Starts Multiple Times:
1. Check browser console for "⚠️ Round 2 already started, skipping duplicate call"
2. If you DON'T see this message, the new file didn't upload
3. Hard refresh the page (Ctrl+Shift+R or Cmd+Shift+R)
4. Clear browser cache

### If Audio Times Out:
1. Check GitHub - are files actually there?
2. Try accessing file directly: https://jordanskennard-bot.github.io/world-cup-game-quiz-show/intro_music.mp3
3. If 404 error, file isn't on GitHub
4. If slow, files might be too large

### If Questions Wrong Order:
1. You didn't upload the new player-complete.html
2. Upload it now
3. Hard refresh player phones

---

## 📱 TESTING TIPS

1. **Use Incognito/Private Windows** - Prevents caching issues
2. **Check Console on Both Host and Player** - Errors appear in both
3. **Test with Real Phones** - Desktop emulation doesn't catch all issues
4. **Watch Firebase Console** - See what data is being written
5. **Keep Both Files Open** - Compare what's happening on host vs player

---

## ✅ UPLOAD STEPS

1. Go to: https://github.com/jordanskennard-bot/world-cup-game-quiz-show
2. Click on `host-complete.html`
3. Click the pencil icon (Edit)
4. Delete ALL content
5. Copy entire content from downloaded file
6. Paste
7. Scroll to bottom
8. Click "Commit changes"
9. Add message: "Fix Round 2 duplication and timer issues"
10. Click "Commit changes" button

11. Repeat for `player-complete.html`
12. Message: "Fix question order"

---

## 🎯 PRIORITY ORDER

1. **First:** Upload host-complete.html (fixes critical bugs)
2. **Second:** Test Round 2 (should only start once now)
3. **Third:** Upload player-complete.html (fixes question order)
4. **Fourth:** Test full game flow
5. **Fifth:** Report any remaining issues

---

Good luck! The Round 2 duplication issue should be completely fixed now. 🎮⚽
