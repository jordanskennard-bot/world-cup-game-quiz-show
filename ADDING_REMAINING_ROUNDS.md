# FOUL PLAY - ADDING REMAINING ROUNDS
## Complete Implementation Guide for Claude Code

---

## 📊 CURRENT GAME STATE ANALYSIS

### ✅ What's Already Implemented:

**Version 8.0 includes:**
1. ✅ **Round 1:** Quiz Questions (4 questions) - WORKING
2. ✅ **Bonus Round:** Karaoke Challenge - IMPLEMENTED
3. ✅ **Scores Review #1** - WORKING
4. ✅ **Round 2:** Pun Round (30 seconds) - WORKING
5. ✅ **Scores Review #2** - WORKING
6. ✅ **Phase 2: Match Draw** (Telestrations) - IMPLEMENTED
7. ✅ **Scores Review #3** - (implied)
8. ✅ **Round 3: Interview Round** - IMPLEMENTED
9. ✅ **Victory Screen** - IMPLEMENTED

### ❌ What's Missing (Needs Adding):

**Per original specification:**
1. ❌ **Commentary Round** (Phase 3) - NOT STARTED
2. ❌ **Toilet Paper Rounds** (Phase 4) - NOT STARTED
   - Toilet paper alert
   - Bog Rolling the Pitch
   - Goal Post Glory
   - Blow Ball
3. ❌ **Sabotage Mechanics** - NOT STARTED
4. ❌ **Handball Mechanic** - NOT STARTED
5. ❌ **Additional Scores Reviews** - Need insertion points

---

## 🎮 CURRENT GAME FLOW

### What Happens Now:
```
Lobby → Team Selection
  ↓
Round 1: Quiz (4 questions)
  ↓
Bonus Round: Karaoke (if accepted)
  ↓
Scores Review #1
  ↓
Round 2: Pun Round (30 sec)
  ↓
Scores Review #2
  ↓
Match Draw: Telestrations (if 4+ players)
  ↓
Scores Review #3
  ↓
Round 3: Interview Round ← CURRENTLY HERE
  ↓
Victory Screen
```

### Where To Insert New Rounds:
```
Lobby → Team Selection
  ↓
Round 1: Quiz (4 questions)
  ↓
Bonus Round: Karaoke (if accepted)
  ↓
Scores Review #1
  ↓
Round 2: Pun Round (30 sec)
  ↓
Scores Review #2
  ↓
Match Draw: Telestrations (if 4+ players)
  ↓
Scores Review #3
  ↓
>>> INSERT: Commentary Round (NEW) <<<
  ↓
Scores Review #4
  ↓
>>> INSERT: Toilet Paper Alert (NEW) <<<
>>> INSERT: Bog Rolling (NEW) <<<
>>> INSERT: Goal Posts (NEW) <<<
>>> INSERT: Blow Ball (NEW) <<<
  ↓
Scores Review #5
  ↓
Round 3: Interview Round (EXISTING - keep)
  ↓
>>> INSERT: Sabotage Reveals (NEW) <<<
  ↓
Victory Screen (with photos)
```

---

## 🎙️ PHASE 3: COMMENTARY ROUND - DETAILED IMPLEMENTATION

### Overview
- Each team commentates on football footage
- Browser microphone recording
- Playback with video
- Referee scores 1-5 per team

### Game Flow
```
Commentary Intro Screen
  ↓
Team 1 Selection (who will commentate)
  ↓
Team 1 Commentary (record while video plays)
  ↓
Team 1 Playback & Judging
  ↓
Team 2 Selection (who will commentate)
  ↓
Team 2 Commentary (record while video plays)
  ↓
Team 2 Playback & Judging
  ↓
Scores Review #4
```

### Implementation Steps

#### Step 1: Create Commentary Data

**Location:** After ROUND_3_QUESTIONS (around line 1160)

```javascript
// Commentary Round - Video clips
const COMMENTARY_VIDEOS = [
  'commentary_video_1.mp4',
  'commentary_video_2.mp4',
  'commentary_video_3.mp4',
  'commentary_video_4.mp4',
  'commentary_video_5.mp4'
];

// Track used videos to avoid repeats
let usedCommentaryVideos = [];
```

#### Step 2: Create Commentary Intro Screen

**Location:** After Match Draw code (around line 3500)

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// PHASE 3: COMMENTARY ROUND
// ═══════════════════════════════════════════════════════════════════════════

function startCommentaryRound() {
  console.log('🎙️ Starting Commentary Round');
  
  // Show intro screen
  const introDiv = document.createElement('div');
  introDiv.id = 'commentary-intro';
  introDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  introDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 80px; color: var(--motd-gold); text-shadow: 0 0 40px rgba(255,198,41,0.8); margin-bottom: 40px; letter-spacing: 6px;">
      COMMENTARY CHALLENGE
    </div>
    
    <div style="font-family: 'Oswald', sans-serif; font-size: 36px; color: var(--text); margin-bottom: 30px; text-align: center; max-width: 800px;">
      We give you the footage, you give us the commentary
    </div>
    
    <div style="font-size: 120px; margin: 40px 0;">
      🎤
    </div>
    
    <div class="spinner"></div>
  `;
  
  document.body.appendChild(introDiv);
  
  // Play explainer audio
  const explainerAudio = new Audio('commentary_explainer.mp3?v=2');
  explainerAudio.volume = 0.6;
  explainerAudio.play().catch(e => console.log('Explainer failed:', e));
  
  explainerAudio.addEventListener('ended', () => {
    introDiv.remove();
    startCommentaryTeam1();
  });
  
  // Fallback
  setTimeout(() => {
    if (document.getElementById('commentary-intro')) {
      introDiv.remove();
      startCommentaryTeam1();
    }
  }, 12000);
  
  gameRef.update({ 
    commentaryActive: true,
    commentaryCurrentTeam: 1
  });
}

function startCommentaryTeam1() {
  console.log('🏠 Team 1 Commentary Selection');
  
  // Play intro audio
  const introAudio = new Audio('commentary_intro_home.mp3?v=2');
  introAudio.volume = 0.6;
  introAudio.play().catch(e => console.log('Intro failed:', e));
  
  // Show selection screen on host
  const selectionDiv = document.createElement('div');
  selectionDiv.id = 'commentary-selection-1';
  selectionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  selectionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 56px; color: var(--text); margin-bottom: 30px;">
      Team 1 - Select Commentator
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 28px; color: var(--motd-cyan); margin-top: 20px;">
      Waiting for Team 1 player to volunteer...
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(selectionDiv);
  
  gameRef.update({ 
    commentaryTeam1SelectionActive: true 
  });
  
  // Listen for Team 1 commentator selection
  gameRef.child('commentary/team1/commentator').on('value', (snapshot) => {
    const commentatorId = snapshot.val();
    if (commentatorId) {
      selectionDiv.remove();
      gameRef.child('commentary/team1/commentator').off();
      startCommentaryRecording(1, commentatorId);
    }
  });
}

function startCommentaryRecording(teamNumber, commentatorId) {
  console.log(`🎬 Starting Team ${teamNumber} recording`);
  
  // Select unused video
  let videoFile;
  if (usedCommentaryVideos.length >= COMMENTARY_VIDEOS.length) {
    // Reset if all used
    usedCommentaryVideos = [];
  }
  const availableVideos = COMMENTARY_VIDEOS.filter(v => !usedCommentaryVideos.includes(v));
  videoFile = availableVideos[Math.floor(Math.random() * availableVideos.length)];
  usedCommentaryVideos.push(videoFile);
  
  // Show countdown: 3, 2, 1
  showCountdown(3, () => {
    // Show video and record
    playCommentaryVideo(teamNumber, videoFile, commentatorId);
  });
}

function playCommentaryVideo(teamNumber, videoFile, commentatorId) {
  console.log(`🎥 Playing video for Team ${teamNumber}`);
  
  const videoDiv = document.createElement('div');
  videoDiv.id = 'commentary-video';
  videoDiv.style.cssText = 'position: fixed; inset: 0; background: #000; display: flex; align-items: center; justify-content: center; z-index: 10000;';
  videoDiv.innerHTML = `
    <video id="commentary-video-player" 
           src="${videoFile}" 
           style="width: 100%; height: 100%; object-fit: contain;"
           autoplay>
    </video>
  `;
  
  document.body.appendChild(videoDiv);
  
  const video = document.getElementById('commentary-video-player');
  
  gameRef.update({
    [`commentary/team${teamNumber}/videoFile`]: videoFile,
    [`commentary/team${teamNumber}/recordingActive`]: true
  });
  
  // When video ends, move to playback
  video.addEventListener('ended', () => {
    videoDiv.remove();
    gameRef.update({
      [`commentary/team${teamNumber}/recordingActive`]: false
    });
    
    // Wait for recording upload
    setTimeout(() => {
      showCommentaryPlayback(teamNumber, videoFile);
    }, 2000);
  });
}

function showCommentaryPlayback(teamNumber, videoFile) {
  console.log(`🔊 Playing back Team ${teamNumber} commentary`);
  
  // Play review intro
  const reviewAudio = new Audio('commentary_review.mp3?v=2');
  reviewAudio.volume = 0.6;
  reviewAudio.play().catch(e => console.log('Review failed:', e));
  
  reviewAudio.addEventListener('ended', () => {
    // Show video with recorded commentary
    const playbackDiv = document.createElement('div');
    playbackDiv.id = 'commentary-playback';
    playbackDiv.style.cssText = 'position: fixed; inset: 0; background: #000; display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000;';
    playbackDiv.innerHTML = `
      <div style="padding: 20px; background: rgba(26,43,74,0.95); width: 100%; text-align: center;">
        <div style="font-family: 'Bebas Neue', sans-serif; font-size: 36px; color: var(--text);">
          Team ${teamNumber} Commentary Playback
        </div>
      </div>
      
      <video id="playback-video" 
             src="${videoFile}" 
             style="flex: 1; width: 100%; object-fit: contain;"
             autoplay>
      </video>
      
      <div style="padding: 20px; background: rgba(26,43,74,0.95); width: 100%; text-align: center;">
        <div style="font-family: 'Barlow', sans-serif; font-size: 24px; color: var(--motd-cyan);">
          Referee is scoring...
        </div>
      </div>
    `;
    
    document.body.appendChild(playbackDiv);
    
    gameRef.update({
      [`commentary/team${teamNumber}/playbackActive`]: true
    });
    
    const playbackVideo = document.getElementById('playback-video');
    
    // Play recorded audio in sync
    gameRef.child(`commentary/team${teamNumber}/recordingURL`).once('value', (snapshot) => {
      const recordingURL = snapshot.val();
      if (recordingURL) {
        const commentaryAudio = new Audio(recordingURL);
        commentaryAudio.play().catch(e => console.log('Commentary playback failed:', e));
      }
    });
    
    // When video ends, wait for referee score
    playbackVideo.addEventListener('ended', () => {
      gameRef.child(`commentary/team${teamNumber}/score`).on('value', (snapshot) => {
        const score = snapshot.val();
        if (score !== null && score !== undefined) {
          playbackDiv.remove();
          gameRef.child(`commentary/team${teamNumber}/score`).off();
          
          // Award points
          const teamPlayers = Object.entries(players).filter(([id, p]) => p.team === teamNumber);
          teamPlayers.forEach(([pid]) => {
            gameRef.child(`players/${pid}/score`).transaction((current) => {
              return (current || 0) + score;
            });
          });
          
          // Move to next team or finish
          if (teamNumber === 1) {
            setTimeout(() => startCommentaryTeam2(), 2000);
          } else {
            setTimeout(() => showScoresReview(), 2000);
          }
        }
      });
    });
  });
}

function startCommentaryTeam2() {
  console.log('✈️ Team 2 Commentary Selection');
  
  // Similar to Team 1 but for Team 2
  // Play away intro
  const introAudio = new Audio('commentary_intro_away.mp3?v=2');
  introAudio.volume = 0.6;
  introAudio.play().catch(e => console.log('Intro failed:', e));
  
  // Show selection screen
  const selectionDiv = document.createElement('div');
  selectionDiv.id = 'commentary-selection-2';
  selectionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  selectionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 56px; color: var(--text); margin-bottom: 30px;">
      Team 2 - Select Commentator
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 28px; color: var(--motd-cyan); margin-top: 20px;">
      Waiting for Team 2 player to volunteer...
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(selectionDiv);
  
  gameRef.update({ 
    commentaryTeam2SelectionActive: true 
  });
  
  // Listen for Team 2 commentator selection
  gameRef.child('commentary/team2/commentator').on('value', (snapshot) => {
    const commentatorId = snapshot.val();
    if (commentatorId) {
      selectionDiv.remove();
      gameRef.child('commentary/team2/commentator').off();
      startCommentaryRecording(2, commentatorId);
    }
  });
}
```

#### Step 3: Microphone Recording (Player Side)

**This is complex - requires:**
- MediaRecorder API
- Permission handling
- Audio blob upload to Firebase Storage
- Fallback if denied

**Key Challenge:** Microphone recording requires browser permissions and can fail

---

## 🧻 PHASE 4: TOILET PAPER ROUNDS - DETAILED IMPLEMENTATION

### Overview
- Physical game mechanics
- Photo upload system
- Multiple mini-games
- Secret sabotage tasks

### Game Flow
```
Toilet Paper Alert (get supplies)
  ↓
Sabotage Task Assignment (secret)
  ↓
Bog Rolling the Pitch (60 seconds)
  ↓
Goal Post Glory (45 seconds)
  ↓
Blow Ball (with photos every 10 seconds)
  ↓
Judging & Points
  ↓
Sabotage Reveals
  ↓
Scores Review #5
```

### Implementation Steps

#### Step 1: Toilet Paper Alert

**Location:** After Commentary Round (around line 3700)

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// PHASE 4: TOILET PAPER ROUNDS
// ═══════════════════════════════════════════════════════════════════════════

function showToiletPaperAlert() {
  console.log('🧻 Showing toilet paper alert');
  
  const alertDiv = document.createElement('div');
  alertDiv.id = 'toilet-paper-alert';
  alertDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  alertDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 80px; color: #ffc629; text-shadow: 0 0 40px rgba(255,198,41,0.8); margin-bottom: 40px; letter-spacing: 6px;">
      ⚠️ IMPORTANT! ⚠️
    </div>
    
    <div style="font-size: 150px; margin: 40px 0;">
      🧻 🧻
    </div>
    
    <div style="font-family: 'Oswald', sans-serif; font-size: 36px; color: var(--text); text-align: center; max-width: 800px;">
      You're going to need toilet paper!
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(alertDiv);
  
  // Play sound effect FIRST
  const soundEffect = new Audio('Toilet_paper_alert.mp3?v=2');
  soundEffect.volume = 0.6;
  soundEffect.play().catch(e => console.log('Sound effect failed:', e));
  
  // When sound effect ends, play voice alert
  soundEffect.addEventListener('ended', () => {
    const voiceAlert = new Audio('toilet_paper_alert.mp3?v=2');
    voiceAlert.volume = 0.6;
    voiceAlert.play().catch(e => console.log('Voice alert failed:', e));
    
    voiceAlert.addEventListener('ended', () => {
      // Assign sabotage tasks before continuing
      assignSabotageTasks();
      
      // Wait for Player 1 ready confirmation
      alertDiv.innerHTML += `
        <div style="margin-top: 40px; font-family: 'Barlow', sans-serif; font-size: 24px; color: var(--motd-cyan);">
          Waiting for Player 1 to confirm ready...
        </div>
      `;
    });
  });
  
  gameRef.update({ toiletPaperAlertActive: true });
  
  // Listen for ready confirmation
  gameRef.child('toiletPaperReady').on('value', (snapshot) => {
    if (snapshot.val() === true) {
      alertDiv.remove();
      gameRef.child('toiletPaperReady').off();
      startBogRolling();
    }
  });
}

function assignSabotageTasks() {
  console.log('🕵️ Assigning sabotage tasks');
  
  // Get players by team
  const team1Players = Object.keys(players).filter(pid => players[pid].team === 1);
  const team2Players = Object.keys(players).filter(pid => players[pid].team === 2);
  
  // Assign tasks (max 2 per team based on spec)
  const sabotagePool = [
    'clean_sheet',
    'on_bench',
    'take_dive',
    'pitch_invasion'
  ];
  
  // Random assignment
  if (team1Players.length > 0) {
    const randomPlayer1 = team1Players[Math.floor(Math.random() * team1Players.length)];
    gameRef.child(`sabotage/${randomPlayer1}`).set({
      task: sabotagePool[0],
      assigned: true,
      completed: false
    });
  }
  
  if (team2Players.length > 0) {
    const randomPlayer2 = team2Players[Math.floor(Math.random() * team2Players.length)];
    gameRef.child(`sabotage/${randomPlayer2}`).set({
      task: sabotagePool[1],
      assigned: true,
      completed: false
    });
  }
}

function startBogRolling() {
  console.log('🧻 Starting Bog Rolling the Pitch');
  
  // Show explainer
  const explainerDiv = document.createElement('div');
  explainerDiv.id = 'bog-explainer';
  explainerDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  explainerDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 72px; color: var(--motd-gold); text-shadow: 0 0 40px rgba(255,198,41,0.8); margin-bottom: 40px;">
      BOG ROLLING THE PITCH
    </div>
    
    <div style="font-family: 'Oswald', sans-serif; font-size: 32px; color: var(--text); text-align: center; max-width: 800px; line-height: 1.5;">
      You have ONE MINUTE to make a football pitch<br>
      out of toilet paper!<br><br>
      Each team does one half.<br>
      Points for accuracy and flair!
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(explainerDiv);
  
  const explainerAudio = new Audio('bog_rolling_explainer.mp3?v=2');
  explainerAudio.volume = 0.6;
  explainerAudio.play().catch(e => console.log('Explainer failed:', e));
  
  explainerAudio.addEventListener('ended', () => {
    explainerDiv.remove();
    startBogRollingTimer();
  });
  
  setTimeout(() => {
    if (document.getElementById('bog-explainer')) {
      explainerDiv.remove();
      startBogRollingTimer();
    }
  }, 12000);
}

function startBogRollingTimer() {
  console.log('⏱️ Starting 60-second bog rolling timer');
  
  const timerDiv = document.createElement('div');
  timerDiv.id = 'bog-timer';
  timerDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  timerDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: var(--text); margin-bottom: 20px;">
      Bog Rolling the Pitch
    </div>
    
    <div id="bog-time" style="font-family: 'Bebas Neue', sans-serif; font-size: 150px; color: var(--motd-gold); text-shadow: 0 0 40px rgba(255,198,41,0.8);">
      60
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 24px; color: rgba(255,255,255,0.7);">
      seconds remaining
    </div>
  `;
  
  document.body.appendChild(timerDiv);
  
  // Start 30-second music (loops twice = 60 seconds)
  const musicAudio = new Audio('bog_rolling_60sec.mp3?v=2');
  musicAudio.volume = 0.5;
  musicAudio.loop = true;
  musicAudio.play().catch(e => console.log('Music failed:', e));
  window.bogRollingMusic = musicAudio;
  
  let timeLeft = 60;
  gameRef.update({ bogRollingTimeLeft: 60 });
  
  const interval = setInterval(() => {
    timeLeft--;
    const timeEl = document.getElementById('bog-time');
    if (timeEl) timeEl.textContent = timeLeft;
    gameRef.update({ bogRollingTimeLeft: timeLeft });
    
    if (timeLeft <= 0) {
      clearInterval(interval);
      
      if (window.bogRollingMusic) {
        window.bogRollingMusic.pause();
        window.bogRollingMusic = null;
      }
      
      timerDiv.remove();
      showBogRollingJudging();
    }
  }, 1000);
}

function showBogRollingJudging() {
  console.log('⚖️ Judging Bog Rolling');
  
  const judgingDiv = document.createElement('div');
  judgingDiv.id = 'bog-judging';
  judgingDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  judgingDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 72px; color: var(--text); margin-bottom: 30px;">
      Time's Up! 📢
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 28px; color: var(--motd-cyan); margin-top: 20px;">
      Referee is scoring both teams...
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(judgingDiv);
  
  gameRef.update({ bogRollingJudgingActive: true });
  
  // Wait for both team scores
  gameRef.child('bogRolling/scores').on('value', (snapshot) => {
    const scores = snapshot.val();
    if (scores && scores.team1 !== undefined && scores.team2 !== undefined) {
      judgingDiv.remove();
      gameRef.child('bogRolling/scores').off();
      
      // Award points to all players on each team
      Object.entries(players).forEach(([pid, player]) => {
        const teamScore = player.team === 1 ? scores.team1 : scores.team2;
        gameRef.child(`players/${pid}/score`).transaction((current) => {
          return (current || 0) + teamScore;
        });
      });
      
      // Move to Goal Posts
      setTimeout(() => startGoalPosts(), 2000);
    }
  });
}

// Similar implementations for Goal Posts and Blow Ball...
```

---

## 🎯 INSERTION POINTS IN CURRENT CODE

### Where to Add Commentary Round

**Current code at line 3951:**
```javascript
setTimeout(() => {
  // After Match Draw, go to Round 3 (Interview)
  startRound3();
}, 2000);
```

**Change to:**
```javascript
setTimeout(() => {
  // After Match Draw, go to Commentary Round
  startCommentaryRound();
}, 2000);
```

### Where to Add Toilet Paper Rounds

**In `startRound3()` function (line 2965), BEFORE showing Interview:**

Add check:
```javascript
function startRound3() {
  // Check if toilet paper rounds were completed
  if (!toiletPaperRoundsComplete) {
    showToiletPaperAlert();
    return;
  }
  
  // Continue with Interview Round
  document.getElementById('game-screen').classList.remove('active');
  document.getElementById('round3-screen').classList.add('active');
  // ... rest of code
}
```

Or better: Insert between Commentary and Interview:

**After Commentary finishes (in final commentary scoring):**
```javascript
setTimeout(() => {
  showScoresReview(); // Scores Review #4
  
  // Then start Toilet Paper rounds
  setTimeout(() => {
    showToiletPaperAlert();
  }, 5000);
}, 2000);
```

---

## 📁 NEW FIREBASE STRUCTURE NEEDED

```javascript
{
  // Existing structure...
  
  // NEW: Commentary Round
  commentary: {
    active: true,
    currentTeam: 1,
    team1: {
      commentator: 'player1',
      videoFile: 'commentary_video_2.mp4',
      recordingURL: 'gs://...',
      score: 4
    },
    team2: {
      commentator: 'player3',
      videoFile: 'commentary_video_5.mp4',
      recordingURL: 'gs://...',
      score: 3
    }
  },
  
  // NEW: Toilet Paper Rounds
  toiletPaper: {
    alertActive: true,
    ready: false,
    bogRolling: {
      active: true,
      timeLeft: 45,
      scores: {
        team1: 4,
        team2: 3
      }
    },
    goalPosts: {
      scores: {
        team1: 5,
        team2: 4
      }
    },
    blowBall: {
      photos: {
        player1: ['url1', 'url2'],
        player2: ['url1', 'url2']
      },
      scores: {
        team1: 3,
        team2: 5
      }
    }
  },
  
  // NEW: Sabotage System
  sabotage: {
    player1: {
      task: 'clean_sheet',
      assigned: true,
      completed: true,
      points: 8
    },
    player2: {
      task: 'on_bench',
      assigned: true,
      completed: false,
      points: 0
    }
  }
}
```

---

## 🎵 AUDIO FILES NEEDED FOR NEW ROUNDS

### Commentary Round (4 files + 5 videos)
- commentary_explainer.mp3
- commentary_intro_home.mp3
- commentary_intro_away.mp3
- commentary_review.mp3
- commentary_video_1.mp4 through commentary_video_5.mp4

### Toilet Paper Rounds (8 files)
- Toilet_paper_alert.mp3 (sound effect)
- toilet_paper_alert.mp3 (voice)
- bog_rolling_explainer.mp3
- bog_rolling_60sec.mp3 (30 sec, loops)
- goal_posts_explainer.mp3
- goal_posts_45sec.mp3
- blowball_explainer.mp3
- blowball_10sec.mp3

---

## 🚀 IMPLEMENTATION PRIORITY

### OPTION A: Commentary First (Harder)
1. Implement Commentary Round
2. Test microphone recording
3. Then add Toilet Paper rounds
4. Test photo upload
5. Add Sabotage system

### OPTION B: Toilet Paper First (Easier)
1. Implement Toilet Paper Alert
2. Implement Bog Rolling (simpler, no mic/camera)
3. Implement Goal Posts
4. Test physical game flow
5. THEN tackle Commentary (complex)
6. Finally add Blow Ball with photos

### RECOMMENDED: Option B
Start with easier toilet paper rounds (except Blow Ball photos), get those working, then add complex Commentary and photo features.

---

## ⚠️ TECHNICAL CHALLENGES

### Commentary Round Challenges:
1. **Microphone Recording:**
   - Requires MediaRecorder API
   - Needs permission handling
   - Must handle denial gracefully
   - Need to upload audio blob to Firebase Storage

2. **Audio Playback Sync:**
   - Video + recorded audio must stay in sync
   - Latency issues possible

3. **Storage:**
   - Need Firebase Storage configured
   - Audio files can be large

### Toilet Paper Challenges:
1. **Photo Upload:**
   - Blow Ball requires camera access
   - Must upload photos to Firebase Storage
   - Display photos at end

2. **Physical Game:**
   - Can't verify actual activity
   - Relies on honor system
   - Referee must be present to judge

### Sabotage Challenges:
1. **Secret Tasks:**
   - Must show only to assigned player
   - Track completion
   - Reveal at end

---

## 📋 STEP-BY-STEP IMPLEMENTATION GUIDE

### Phase A: Prepare Infrastructure (DO FIRST)

**Task A1: Add Firebase Storage**
- Enable Firebase Storage in console
- Update Firebase initialization
- Test file upload capability

**Task A2: Create Helper Functions**
- Countdown function (reusable)
- Photo upload function
- Audio recording function
- Score display function

### Phase B: Implement Toilet Paper Alert (EASY)

**Task B1: Add Toilet Paper Alert Screen**
- Location: After Commentary (or after Match Draw if skipping Commentary)
- Play dual audio (sound effect + voice)
- Wait for Player 1 confirmation
- Move to Bog Rolling

**Task B2: Implement Sabotage Assignment**
- Random player selection
- Secret task notification (player-side)
- Track assigned tasks

### Phase C: Implement Bog Rolling (MEDIUM)

**Task C1: Add Bog Rolling Explainer**
- Screen with rules
- Audio explanation
- Transition to timer

**Task C2: Add 60-Second Timer**
- Display countdown
- Play looping 30-second music
- Stop at 0

**Task C3: Add Referee Judging**
- Show judging screen on host
- Referee scores both teams (1-5)
- Award points
- Move to Goal Posts

### Phase D: Implement Goal Posts & Blow Ball (HARD)

**Task D1: Goal Posts Round**
- Similar to Bog Rolling but 45 seconds
- Different scoring criteria

**Task D2: Blow Ball with Photos**
- Requires camera implementation
- Photo every 10 seconds
- Emotion display
- Upload and store photos

### Phase E: Implement Commentary (VERY HARD)

**Task E1: Microphone Permission Handling**
- Request mic access
- Handle denial gracefully
- Offer to next player if denied

**Task E2: Recording Implementation**
- MediaRecorder setup
- Record while video plays
- Save audio blob
- Upload to Firebase Storage

**Task E3: Playback Implementation**
- Play video
- Play recorded audio in sync
- Handle timing issues

---

## ✅ SUCCESS CRITERIA

**Commentary Round Working:**
- [ ] Players can select commentator
- [ ] Microphone recording works
- [ ] Video plays while recording
- [ ] Playback syncs audio + video
- [ ] Referee can score
- [ ] Points awarded correctly

**Toilet Paper Rounds Working:**
- [ ] Alert screen shows
- [ ] Sabotage tasks assigned
- [ ] Bog Rolling timer works (60 sec)
- [ ] Music loops correctly
- [ ] Referee judging works
- [ ] Goal Posts works (45 sec)
- [ ] Blow Ball photos upload
- [ ] All points awarded correctly

**Full Game Flow:**
- [ ] Round 1 → Bonus → Scores
- [ ] Round 2 → Scores
- [ ] Match Draw → Scores
- [ ] Commentary → Scores
- [ ] Toilet Paper → Scores
- [ ] Interview → Sabotage Reveal
- [ ] Victory Screen with photos

---

## 🎯 RECOMMENDED APPROACH FOR CLAUDE CODE

**Week 1: Infrastructure**
- Set up Firebase Storage
- Create helper functions
- Test upload/download

**Week 2: Toilet Paper (No Photos)**
- Alert screen
- Sabotage assignment
- Bog Rolling (complete)
- Goal Posts (complete)
- Skip Blow Ball for now

**Week 3: Commentary (Complex)**
- Mic permission handling
- Recording implementation
- Playback sync
- Full testing

**Week 4: Photos & Polish**
- Camera implementation
- Blow Ball with photos
- Victory screen photo album
- Full game testing

---

END OF REMAINING ROUNDS IMPLEMENTATION GUIDE
READY FOR CLAUDE CODE! 🎮⚽✨
