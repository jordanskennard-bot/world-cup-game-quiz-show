# COMMENTARY ROUND - IMPLEMENTATION INSTRUCTIONS FOR CLAUDE CODE
## Complete Step-by-Step Guide

---

## 🎯 OBJECTIVE

Implement the Commentary Round where each team commentates on football footage using their microphone.

---

## 📋 GAME FLOW

```
Match Draw completes
  ↓
Commentary Round Intro (explainer audio)
  ↓
Home Team (Team 1) Selection
  ↓
Home Team Recording (20-30 sec video)
  ↓
Home Team Playback & Referee Scoring (1-5 points)
  ↓
Away Team (Team 2) Selection
  ↓
Away Team Recording (20-30 sec video)
  ↓
Away Team Playback & Referee Scoring (1-5 points)
  ↓
Toilet Paper Alert
```

---

## 📁 AUDIO/VIDEO FILES AVAILABLE

**Audio:**
- commentary_explainer.mp3
- commentary_intro_home.mp3
- commentary_intro_away.mp3
- commentary_review.mp3

**Video:**
- commentary_video_2.mp4
- commentary_video_3.mp4
- commentary_video_4.mp4
- commentary_video_5.mp4
- commentary_video_6.mp4

---

## 🔧 IMPLEMENTATION

---

## STEP 1: Add Commentary Data

**File:** `host-complete_42.html`
**Location:** After ROUND_3_QUESTIONS (line ~1160)

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// COMMENTARY ROUND - DATA
// ═══════════════════════════════════════════════════════════════════════════

const COMMENTARY_VIDEOS = [
  'commentary_video_2.mp4',
  'commentary_video_3.mp4',
  'commentary_video_4.mp4',
  'commentary_video_5.mp4',
  'commentary_video_6.mp4'
];

let usedCommentaryVideos = [];
```

---

## STEP 2: Update Match Draw Transition

**File:** `host-complete_42.html`
**Location:** Line ~3951 (search for "After Match Draw")

**Change from:**
```javascript
setTimeout(() => {
  startRound3();
}, 2000);
```

**Change to:**
```javascript
setTimeout(() => {
  startCommentaryRound();
}, 2000);
```

---

## STEP 3: Add Host Commentary Functions

**File:** `host-complete_42.html`
**Location:** After Match Draw, before Toilet Paper (line ~3500)

**Add complete section - see full code in attached document**

Key functions to add:
- `startCommentaryRound()` - Shows intro
- `startCommentaryTeamSelection(teamNumber)` - Team selects commentator
- `startCommentaryRecording(teamNumber, commentatorId)` - Countdown
- `playCommentaryVideo(teamNumber, videoFile)` - Shows video, records audio
- `playbackCommentary(teamNumber, videoFile)` - Plays back with commentary

---

## STEP 4: Add Player Commentary Functions

**File:** `player-complete_27.html`
**Location:** After existing listeners (line ~1300)

**Add complete section - see full code in attached document**

Key functions to add:
- Firebase listeners for selection/recording/playback
- `showCommentatorVolunteer(teamNumber)` - "I'm Up" button
- `volunteerAsCommentator(teamNumber)` - First to click
- `startMicRecording(teamNumber)` - Uses MediaRecorder API
- `uploadRecording(audioBlob, teamNumber)` - Saves to Firebase
- `showRefereeCommentaryScoring(teamNumber)` - Referee scores 1-5

---

## ⚠️ IMPORTANT NOTES

### **Microphone Recording:**
- Uses `navigator.mediaDevices.getUserMedia()`
- Requires HTTPS (works on GitHub Pages)
- Browser will ask for permission
- If denied, game continues without audio

### **Video Selection:**
- Random video from pool
- Tracks used videos to avoid repeats
- Resets when all 5 used

### **Timeouts:**
- 30 seconds to volunteer (or -5 points penalty)
- 30 seconds for referee to score (or auto-continues)

### **Referee:**
- Always Player 1
- Scores 1-5 for each team
- Points awarded to ALL team members

---

## 🎮 DETAILED GAME FLOW

### **1. Commentary Intro**
- Host: Shows "COMMENTARY CHALLENGE" title + mic emoji
- Audio: commentary_explainer.mp3
- Players: See same screen
- Duration: ~10 seconds

### **2. Team 1 Selection**
- Host: "Team 1 - Select Commentator" + spinner
- Audio: commentary_intro_home.mp3
- Players (Team 1): See "I'm Up!" and "Not Me" buttons
- Players (Team 2): Waiting screen
- First to click "I'm Up" becomes commentator
- Timeout: 30 seconds (-5 points if nobody volunteers)

### **3. Team 1 Recording**
- Host: 3-2-1 countdown, then video plays with "🔴 RECORDING"
- Commentator: Sees recording indicator, mic activates
- Other Players: Waiting screen
- Duration: Video length (20-30 seconds)

### **4. Team 1 Playback**
- Host: "Let's see how you got on" audio, then video + recorded audio
- Referee (Player 1): Sees scoring buttons (1-5)
- Other Players: "Watch the screen"
- Points awarded to all Team 1 members

### **5. Team 2 (Repeat)**
- Same as Team 1 but with:
  - commentary_intro_away.mp3
  - Different video from pool
  - Team 2 members volunteer

### **6. After Both Teams**
- Moves to Toilet Paper Alert

---

## 🔄 FIREBASE STRUCTURE

Auto-created during game:

```
commentary/
  team1/
    commentator: "player_id"
    videoFile: "commentary_video_2.mp4"
    recordingURL: "data:audio/webm;base64,..."
    score: 4
  team2/
    commentator: "player_id"
    videoFile: "commentary_video_5.mp4"
    recordingURL: "data:audio/webm;base64,..."
    score: 3

commentaryTeam1SelectionActive: true/false
commentaryTeam2SelectionActive: true/false
```

---

## ✅ TESTING CHECKLIST

- [ ] Match Draw ends → Commentary Intro shows
- [ ] Explainer audio plays
- [ ] Team 1 selection screen appears
- [ ] Team 1 players see "I'm Up" button
- [ ] First click registers correctly
- [ ] 3-2-1 countdown displays
- [ ] Video plays on host
- [ ] Mic recording works on commentator's phone
- [ ] Red recording indicator shows
- [ ] Video ends automatically
- [ ] Playback screen shows
- [ ] Recorded audio plays with video
- [ ] Referee sees 1-5 buttons
- [ ] Clicking score registers
- [ ] Points awarded to all Team 1 members
- [ ] Team 2 selection starts automatically
- [ ] Same flow works for Team 2
- [ ] After Team 2 scoring → Toilet Paper Alert
- [ ] No console errors throughout

---

## 🚨 ERROR HANDLING

### **Already Implemented:**

1. **No volunteer within 30 seconds:**
   - Deducts 5 points from team
   - Moves to next team/round

2. **Microphone permission denied:**
   - Shows alert to user
   - Continues with silent commentary
   - Game doesn't break

3. **Recording upload fails:**
   - Logs error
   - Continues without audio
   - Playback shows video only

4. **Referee doesn't score within 30 seconds:**
   - Auto-continues to next team
   - No points awarded

5. **Video fails to load:**
   - Fallback timeout triggers
   - Moves forward anyway

---

## 📱 MOBILE CONSIDERATIONS

- Microphone works on mobile browsers (Safari, Chrome)
- HTTPS required (GitHub Pages provides this)
- First-time mic permission prompt may be confusing
- Recording quality varies by device
- Video playback should work on all modern phones

---

## 🎯 SUCCESS CRITERIA

**Working correctly when:**
1. Both teams can select commentators
2. Videos play smoothly
3. Microphone recording works (or gracefully fails)
4. Playback includes recorded audio
5. Referee can score both teams
6. Points update correctly
7. Game transitions to Toilet Paper Alert
8. No crashes or freezes

---

## ⏱️ ESTIMATED TIME

- **Code Implementation:** 30-40 minutes
- **Testing & Debugging:** 15-20 minutes
- **Total:** ~1 hour

---

## 💡 TIPS FOR CLAUDE CODE

1. **Copy entire code blocks** - don't type from scratch
2. **Keep line numbers consistent** - use provided locations
3. **Test incrementally** - check after each major function
4. **Check browser console** - logs will show progress
5. **Use exact function names** - case-sensitive
6. **Don't modify existing code** - only add new sections
7. **Verify file paths** - videos must be in same folder as HTML

---

## 📦 FINAL DELIVERABLES

After implementation, you should have:
- ✅ Updated host-complete_42.html (with new functions)
- ✅ Updated player-complete_27.html (with new functions)
- ✅ All audio files uploaded to GitHub
- ✅ All video files uploaded to GitHub
- ✅ Tested with real phones
- ✅ Confirmed microphone recording works
- ✅ Verified smooth game flow

---

END OF COMMENTARY ROUND IMPLEMENTATION GUIDE
Ready for Claude Code! 🎙️⚽✨
