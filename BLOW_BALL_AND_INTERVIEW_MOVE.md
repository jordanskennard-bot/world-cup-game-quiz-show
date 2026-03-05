# CLAUDE CODE: IMPLEMENT BLOW BALL + MOVE INTERVIEW ROUND
## Step-by-Step Implementation Instructions

---

## 🎯 OBJECTIVES

**Part A: Move Interview Round**
- Move Interview Round from after Toilet Paper rounds to after Round 2 (Puns)
- Update game flow routing

**Part B: Implement Blow Ball**
- Add Blow Ball round after Goal Posts
- Camera photo capture every 10 seconds
- 6 different emotions to display
- Photo upload to Firebase
- Referee scoring

---

## 📊 NEW GAME FLOW

### **BEFORE:**
```
Round 1 → Bonus → Scores #1
  ↓
Round 2 (Puns) → Scores #2
  ↓
Match Draw → Scores #3
  ↓
Commentary → Scores #4
  ↓
Toilet Paper Alert → Bog Rolling → Goal Posts
  ↓
Interview Round
  ↓
Victory Screen
```

### **AFTER:**
```
Round 1 → Bonus → Scores #1
  ↓
Round 2 (Puns) → Scores #2
  ↓
🆕 Interview Round (MOVED HERE)
  ↓
Scores #3
  ↓
Match Draw → Scores #4
  ↓
Commentary → Scores #5
  ↓
Toilet Paper Alert → Bog Rolling → Goal Posts
  ↓
🆕 Blow Ball (with photos)
  ↓
Scores #6
  ↓
Sabotage Reveals
  ↓
Victory Screen (with photo album)
```

---

# PART A: MOVE INTERVIEW ROUND

## 📝 STEP A1: UPDATE SCORES REVIEW ROUTING

**File:** `host-complete_42.html`
**Location:** In `showScoresReview()` function, find the routing switch (around line 2440)

**Find this code:**
```javascript
switch(source) {
  case 'round1':
    startRound2();
    break;
  case 'round2':
    checkForMatchDraw();
    break;
  case 'matchdraw':
    startCommentaryRound();
    break;
  case 'commentary':
    showToiletPaperAlert();
    break;
  case 'toiletpaper':
    startRound3();
    break;
  default:
    startRound2();
}
```

**Replace with:**
```javascript
switch(source) {
  case 'round1':
    startRound2();
    break;
  case 'round2':
    startRound3(); // Go to Interview Round
    break;
  case 'interview':
    checkForMatchDraw(); // Then Match Draw
    break;
  case 'matchdraw':
    startCommentaryRound();
    break;
  case 'commentary':
    showToiletPaperAlert();
    break;
  case 'toiletpaper':
    showSabotageReveals(); // Skip interview, go to sabotage
    break;
  default:
    startRound2();
}
```

---

## 📝 STEP A2: UPDATE INTERVIEW ROUND TO GO TO SCORES REVIEW

**File:** `host-complete_42.html`
**Location:** Find `nextRound3Question()` function (around line 3110)

**Find this code:**
```javascript
function nextRound3Question() {
  round3CurrentQ++;
  if (round3CurrentQ < ROUND_3_QUESTIONS.length) {
    loadRound3Question(round3CurrentQ);
  } else {
    // Round 3 (Interview) complete → Sabotage Reveals
    console.log('✅ Interview Round complete, showing sabotage reveals');
    showSabotageReveals();
  }
}
```

**Replace with:**
```javascript
function nextRound3Question() {
  round3CurrentQ++;
  if (round3CurrentQ < ROUND_3_QUESTIONS.length) {
    loadRound3Question(round3CurrentQ);
  } else {
    // Round 3 (Interview) complete → Scores Review
    console.log('✅ Interview Round complete, showing scores review');
    window.scoresReviewSource = 'interview';
    showScoresReview();
  }
}
```

---

# PART B: IMPLEMENT BLOW BALL ROUND

## 📝 STEP B1: ADD BLOW BALL DATA

**File:** `host-complete_42.html`
**Location:** After Goal Posts functions (around line 4300)

**Add this code:**

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// BLOW BALL ROUND
// ═══════════════════════════════════════════════════════════════════════════

const BLOW_BALL_EMOTIONS = [
  '😐 Serious',
  '😕 Confused',
  '😣 In Pain',
  '🤩 Excited',
  '🤤 Hungry',
  '😊 Happy'
];

let blowBallCurrentEmotion = 0;
let blowBallPhotoCount = 0;
const TOTAL_BLOW_BALL_PHOTOS = 6;
```

---

## 📝 STEP B2: UPDATE GOAL POSTS TO GO TO BLOW BALL

**File:** `host-complete_42.html`
**Location:** In `showGoalPostsJudging()` function (around line 4270)

**Find where it moves to next round after judging:**
```javascript
// Move to Blow Ball (or skip to Scores Review if not implemented)
setTimeout(() => {
  showScoresReviewAfterToiletPaper();
}, 2000);
```

**Replace with:**
```javascript
// Move to Blow Ball
setTimeout(() => {
  startBlowBall();
}, 2000);
```

---

## 📝 STEP B3: ADD BLOW BALL FUNCTIONS (HOST)

**File:** `host-complete_42.html`
**Location:** After Goal Posts judging function

**Add this complete section:**

```javascript
function startBlowBall() {
  console.log('💨 Starting Blow Ball');
  
  const explainerDiv = document.createElement('div');
  explainerDiv.id = 'blowball-explainer';
  explainerDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  explainerDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 72px; color: var(--motd-gold); text-shadow: 0 0 40px rgba(255,198,41,0.8); margin-bottom: 40px;">
      BLOW BALL
    </div>
    
    <div style="font-family: 'Oswald', sans-serif; font-size: 28px; color: var(--text); text-align: center; max-width: 900px; line-height: 1.5; margin-bottom: 40px;">
      Both teams must take a single piece of toilet paper<br>
      and using only your breath, propel it from your goal<br>
      to your opponent's goal.<br><br>
      Every 10 seconds, STOP and take a photo<br>
      showing the emotion on screen!
    </div>
    
    <div class="spinner"></div>
  `;
  
  document.body.appendChild(explainerDiv);
  
  const explainerAudio = new Audio('blowball_explainer.mp3?v=2');
  explainerAudio.volume = 0.6;
  explainerAudio.play().catch(e => console.log('Explainer audio:', e));
  
  explainerAudio.addEventListener('ended', () => {
    explainerDiv.remove();
    selectPhotographers();
  });
  
  setTimeout(() => {
    if (document.getElementById('blowball-explainer')) {
      explainerDiv.remove();
      selectPhotographers();
    }
  }, 15000);
  
  gameRef.update({ blowBallActive: true });
}

function selectPhotographers() {
  console.log('📸 Selecting team photographers');
  
  const selectionDiv = document.createElement('div');
  selectionDiv.id = 'photographer-selection';
  selectionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  selectionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 56px; color: var(--text); margin-bottom: 30px;">
      Select Team Photographers
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 28px; color: var(--motd-cyan); margin-top: 20px;">
      Waiting for one player from each team...
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(selectionDiv);
  
  gameRef.update({ blowBallPhotographerSelectionActive: true });
  
  // Wait for both photographers
  const checkPhotographers = setInterval(() => {
    gameRef.child('blowBall/photographers').once('value', (snapshot) => {
      const photographers = snapshot.val();
      if (photographers && photographers.team1 && photographers.team2) {
        clearInterval(checkPhotographers);
        selectionDiv.remove();
        startBlowBallRound();
      }
    });
  }, 500);
  
  // Timeout fallback
  setTimeout(() => {
    if (document.getElementById('photographer-selection')) {
      clearInterval(checkPhotographers);
      selectionDiv.remove();
      console.log('⚠️ No photographers selected, skipping Blow Ball');
      finishBlowBall();
    }
  }, 30000);
}

function startBlowBallRound() {
  console.log('💨 Starting Blow Ball emotion rounds');
  
  blowBallCurrentEmotion = 0;
  blowBallPhotoCount = 0;
  
  showNextEmotion();
}

function showNextEmotion() {
  if (blowBallPhotoCount >= TOTAL_BLOW_BALL_PHOTOS) {
    finishBlowBall();
    return;
  }
  
  const emotion = BLOW_BALL_EMOTIONS[blowBallCurrentEmotion];
  
  const emotionDiv = document.createElement('div');
  emotionDiv.id = 'blowball-emotion';
  emotionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  emotionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 56px; color: var(--text); margin-bottom: 30px;">
      Show This Emotion:
    </div>
    
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 120px; color: var(--motd-gold); text-shadow: 0 0 60px rgba(255,198,41,0.8); margin-bottom: 40px;">
      ${emotion}
    </div>
    
    <div id="blowball-timer" style="font-family: 'Bebas Neue', sans-serif; font-size: 80px; color: var(--motd-cyan);">
      10
    </div>
  `;
  
  document.body.appendChild(emotionDiv);
  
  gameRef.update({ 
    blowBallEmotion: emotion,
    blowBallTimeLeft: 10,
    blowBallPhotoRound: blowBallPhotoCount + 1
  });
  
  // Play 10-second audio
  const musicAudio = new Audio('blowball_10sec.mp3?v=2');
  musicAudio.volume = 0.5;
  musicAudio.play().catch(e => console.log('Music:', e));
  
  let timeLeft = 10;
  const interval = setInterval(() => {
    timeLeft--;
    const timerEl = document.getElementById('blowball-timer');
    if (timerEl) timerEl.textContent = timeLeft;
    gameRef.update({ blowBallTimeLeft: timeLeft });
    
    if (timeLeft <= 0) {
      clearInterval(interval);
      emotionDiv.remove();
      
      blowBallPhotoCount++;
      blowBallCurrentEmotion++;
      
      // Brief pause before next emotion
      setTimeout(() => {
        showNextEmotion();
      }, 2000);
    }
  }, 1000);
}

function finishBlowBall() {
  console.log('✅ Blow Ball Complete');
  
  gameRef.update({ 
    blowBallActive: false,
    blowBallComplete: true,
    blowBallJudgingActive: true
  });
  
  // Show judging screen
  const judgingDiv = document.createElement('div');
  judgingDiv.id = 'blowball-judging';
  judgingDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 40px;';
  judgingDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 72px; color: var(--text); margin-bottom: 30px;">
      Full Time! 📢
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 28px; color: var(--motd-cyan); margin-top: 20px;">
      Referee is scoring both teams on speed, flair, and huff...
    </div>
    
    <div class="spinner" style="margin-top: 40px;"></div>
  `;
  
  document.body.appendChild(judgingDiv);
  
  // Wait for both team scores
  const scoreWait = setInterval(() => {
    gameRef.child('blowBall/scores').once('value', (snapshot) => {
      const scores = snapshot.val();
      if (scores && scores.team1 !== undefined && scores.team2 !== undefined) {
        clearInterval(scoreWait);
        judgingDiv.remove();
        
        // Award points to all players on each team
        Object.entries(players).forEach(([pid, player]) => {
          const teamScore = player.team === 1 ? scores.team1 : scores.team2;
          gameRef.child(`players/${pid}/score`).transaction((current) => {
            return (current || 0) + teamScore;
          });
        });
        
        // Show scores review, then sabotage reveals
        setTimeout(() => {
          window.scoresReviewSource = 'toiletpaper';
          showScoresReview();
        }, 2000);
      }
    });
  }, 500);
  
  // Fallback timeout
  setTimeout(() => {
    if (document.getElementById('blowball-judging')) {
      clearInterval(scoreWait);
      judgingDiv.remove();
      window.scoresReviewSource = 'toiletpaper';
      showScoresReview();
    }
  }, 30000);
}
```

---

## 📝 STEP B4: ADD BLOW BALL PLAYER SCREENS

**File:** `player-complete_27.html`
**Location:** After Goal Posts player code (around line 2200)

**Add this complete section:**

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// BLOW BALL - PLAYER
// ═══════════════════════════════════════════════════════════════════════════

// Listen for photographer selection
gameRef.child('blowBallPhotographerSelectionActive').on('value', (snapshot) => {
  if (snapshot.val() === true) {
    showPhotographerSelection();
  } else {
    const selectionDiv = document.getElementById('player-photographer-selection');
    if (selectionDiv) selectionDiv.remove();
  }
});

// Listen for Blow Ball emotions
gameRef.child('blowBallEmotion').on('value', (snapshot) => {
  const emotion = snapshot.val();
  if (emotion) {
    showPlayerBlowBallEmotion(emotion);
  }
});

// Listen for Blow Ball judging
gameRef.child('blowBallJudgingActive').on('value', (snapshot) => {
  if (snapshot.val() === true) {
    showPlayerBlowBallJudging();
  } else {
    const judgingDiv = document.getElementById('player-blowball-judging');
    if (judgingDiv) judgingDiv.remove();
  }
});

function showPhotographerSelection() {
  const existingDiv = document.getElementById('player-photographer-selection');
  if (existingDiv) return;
  
  const selectionDiv = document.createElement('div');
  selectionDiv.id = 'player-photographer-selection';
  selectionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 30px; text-align: center;';
  selectionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: #ffc629; margin-bottom: 30px;">
      📸 Blow Ball
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 22px; color: rgba(255,255,255,0.9); margin-bottom: 40px; line-height: 1.6;">
      Your team needs a photographer!<br>
      They will capture photos every 10 seconds.
    </div>
    
    <button onclick="volunteerAsPhotographer()" 
            style="padding: 20px 50px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 15px; font-family: 'Bebas Neue', sans-serif; font-size: 28px; cursor: pointer; box-shadow: 0 10px 30px rgba(255,198,41,0.4);">
      I'm the Team Photographer!
    </button>
  `;
  
  document.body.appendChild(selectionDiv);
}

function volunteerAsPhotographer() {
  console.log('📸 Volunteering as photographer');
  
  const playerTeam = players[playerId].team;
  gameRef.child(`blowBall/photographers/team${playerTeam}`).set(playerId);
  
  const selectionDiv = document.getElementById('player-photographer-selection');
  if (selectionDiv) selectionDiv.remove();
  
  // Show waiting screen
  const waitDiv = document.createElement('div');
  waitDiv.id = 'waiting-blowball';
  waitDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 30px; text-align: center;';
  waitDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: #4dd4e8; margin-bottom: 30px;">
      Get Ready to Photograph!
    </div>
    
    <div class="spinner"></div>
  `;
  
  document.body.appendChild(waitDiv);
}

function showPlayerBlowBallEmotion(emotion) {
  // Remove waiting screen
  const waitDiv = document.getElementById('waiting-blowball');
  if (waitDiv) waitDiv.remove();
  
  // Check if this player is a photographer
  gameRef.child('blowBall/photographers').once('value', (snapshot) => {
    const photographers = snapshot.val();
    const isPhotographer = photographers && 
      (photographers.team1 === playerId || photographers.team2 === playerId);
    
    if (isPhotographer) {
      showPhotographerScreen(emotion);
    } else {
      showPlayerEmotionScreen(emotion);
    }
  });
}

function showPhotographerScreen(emotion) {
  let emotionDiv = document.getElementById('player-blowball-emotion');
  
  if (!emotionDiv) {
    emotionDiv = document.createElement('div');
    emotionDiv.id = 'player-blowball-emotion';
    emotionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 30px; text-align: center;';
    document.body.appendChild(emotionDiv);
  }
  
  emotionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 42px; color: #fff; margin-bottom: 30px;">
      Show This Emotion:
    </div>
    
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 100px; color: #ffc629; text-shadow: 0 0 40px rgba(255,198,41,0.6); margin-bottom: 40px;">
      ${emotion}
    </div>
    
    <input type="file" 
           accept="image/*" 
           capture="user" 
           id="photo-capture"
           style="display: none;"
           onchange="handlePhotoCapture(this)">
    
    <button onclick="document.getElementById('photo-capture').click()" 
            style="padding: 20px 50px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 15px; font-family: 'Bebas Neue', sans-serif; font-size: 28px; cursor: pointer; box-shadow: 0 10px 30px rgba(255,198,41,0.4);">
      📸 Take Photo
    </button>
    
    <div id="photo-preview" style="margin-top: 30px; display: none;">
      <img id="preview-img" style="max-width: 300px; border-radius: 12px; border: 3px solid #4dd4e8;">
    </div>
  `;
}

function showPlayerEmotionScreen(emotion) {
  let emotionDiv = document.getElementById('player-blowball-emotion');
  
  if (!emotionDiv) {
    emotionDiv = document.createElement('div');
    emotionDiv.id = 'player-blowball-emotion';
    emotionDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 30px; text-align: center;';
    document.body.appendChild(emotionDiv);
  }
  
  emotionDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 42px; color: #fff; margin-bottom: 30px;">
      Show This Emotion:
    </div>
    
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 100px; color: #ffc629; text-shadow: 0 0 40px rgba(255,198,41,0.6); margin-bottom: 40px;">
      ${emotion}
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 20px; color: rgba(255,255,255,0.8);">
      Keep blowing that toilet paper!
    </div>
  `;
}

async function handlePhotoCapture(input) {
  const file = input.files[0];
  if (!file) return;
  
  console.log('📸 Photo captured');
  
  // Show preview
  const reader = new FileReader();
  reader.onload = (e) => {
    const preview = document.getElementById('photo-preview');
    const previewImg = document.getElementById('preview-img');
    if (preview && previewImg) {
      previewImg.src = e.target.result;
      preview.style.display = 'block';
    }
  };
  reader.readAsDataURL(file);
  
  // Upload to Firebase
  try {
    const base64 = await convertToBase64(file);
    
    // Get current photo round
    const photoRound = await gameRef.child('blowBallPhotoRound').once('value');
    const roundNumber = photoRound.val() || 1;
    
    gameRef.child(`blowBall/photos/${playerId}`).push({
      photo: base64,
      round: roundNumber,
      timestamp: Date.now()
    });
    
    console.log('✅ Photo uploaded');
  } catch (error) {
    console.error('❌ Photo upload failed:', error);
  }
}

function convertToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });
}

function showPlayerBlowBallJudging() {
  const emotionDiv = document.getElementById('player-blowball-emotion');
  if (emotionDiv) emotionDiv.remove();
  
  // Check if this player is the referee
  const playerIds = Object.keys(players);
  const refereeId = playerIds[0];
  
  if (playerId === refereeId) {
    showRefereeBlowBallScoring();
  } else {
    showWaitingForBlowBallScoring();
  }
}

function showRefereeBlowBallScoring() {
  const scoringDiv = document.createElement('div');
  scoringDiv.id = 'referee-blowball-scoring';
  scoringDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; padding: 30px; overflow-y: auto; z-index: 10000;';
  scoringDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: #ffc629; margin-bottom: 30px; text-align: center;">
      ⚽ You are the Referee ⚽
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 24px; color: rgba(255,255,255,0.9); margin-bottom: 40px; text-align: center;">
      Score based on speed, flair, and huff!
    </div>
    
    <div style="margin-bottom: 40px; width: 100%; max-width: 500px;">
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 32px; color: #fff; margin-bottom: 20px; text-align: center;">
        Team 1 Score
      </div>
      <div style="display: flex; gap: 15px; justify-content: center;">
        ${[1,2,3,4,5].map(score => `
          <button onclick="setBlowBallTeam1Score(${score})" 
                  style="width: 70px; height: 70px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 50%; font-family: 'Bebas Neue', sans-serif; font-size: 40px; cursor: pointer;">
            ${score}
          </button>
        `).join('')}
      </div>
    </div>
    
    <div style="margin-bottom: 40px; width: 100%; max-width: 500px;">
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 32px; color: #fff; margin-bottom: 20px; text-align: center;">
        Team 2 Score
      </div>
      <div style="display: flex; gap: 15px; justify-content: center;">
        ${[1,2,3,4,5].map(score => `
          <button onclick="setBlowBallTeam2Score(${score})" 
                  style="width: 70px; height: 70px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 50%; font-family: 'Bebas Neue', sans-serif; font-size: 40px; cursor: pointer;">
            ${score}
          </button>
        `).join('')}
      </div>
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 16px; color: rgba(255,255,255,0.6); text-align: center;">
      1 = Poor | 5 = Excellent
    </div>
  `;
  
  document.body.appendChild(scoringDiv);
}

let blowBallTeam1Score = null;
let blowBallTeam2Score = null;

function setBlowBallTeam1Score(score) {
  blowBallTeam1Score = score;
  console.log('Team 1 scored:', score);
  
  if (blowBallTeam2Score !== null) {
    submitBlowBallScores();
  }
}

function setBlowBallTeam2Score(score) {
  blowBallTeam2Score = score;
  console.log('Team 2 scored:', score);
  
  if (blowBallTeam1Score !== null) {
    submitBlowBallScores();
  }
}

function submitBlowBallScores() {
  gameRef.child('blowBall/scores').set({
    team1: blowBallTeam1Score,
    team2: blowBallTeam2Score
  });
  
  const scoringDiv = document.getElementById('referee-blowball-scoring');
  if (scoringDiv) scoringDiv.remove();
  
  showWaitingForBlowBallScoring();
  
  blowBallTeam1Score = null;
  blowBallTeam2Score = null;
}

function showWaitingForBlowBallScoring() {
  const waitDiv = document.createElement('div');
  waitDiv.id = 'waiting-blowball-scoring';
  waitDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 30px; text-align: center;';
  waitDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: #4dd4e8; margin-bottom: 30px;">
      Full Time!
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 22px; color: rgba(255,255,255,0.9);">
      Calculating final scores...
    </div>
  `;
  
  document.body.appendChild(waitDiv);
}
```

---

## 📝 STEP B5: UPDATE VICTORY SCREEN TO SHOW PHOTO ALBUM

**File:** `host-complete_42.html`
**Location:** In `showVictoryScreen()` function (around line 3526)

**Find where victory screen HTML is created and ADD this section AFTER the MVP section:**

```javascript
// Add photo album section
`
<div id="photo-album" style="width: 100%; max-width: 1200px; margin-top: 60px;">
  <!-- Photos will be loaded here -->
</div>
`
```

**Then ADD this function after showVictoryScreen():**

```javascript
function loadPhotoAlbum() {
  gameRef.child('blowBall/photos').once('value', (snapshot) => {
    const photosData = snapshot.val();
    if (!photosData) return;
    
    const albumEl = document.getElementById('photo-album');
    if (!albumEl) return;
    
    let html = `
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: var(--text); margin-bottom: 30px; text-align: center;">
        📸 Photo Album 📸
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px;">
    `;
    
    Object.entries(photosData).forEach(([playerId, playerPhotos]) => {
      const playerName = players[playerId]?.name || 'Unknown';
      
      Object.values(playerPhotos).forEach((photoData) => {
        html += `
          <div style="background: rgba(255,255,255,0.1); border-radius: 12px; padding: 10px; text-align: center;">
            <div style="font-family: 'Barlow', sans-serif; font-size: 16px; color: rgba(255,255,255,0.8); margin-bottom: 8px;">
              ${playerName}
            </div>
            <img src="${photoData.photo}" 
                 style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px;">
          </div>
        `;
      });
    });
    
    html += `</div>`;
    albumEl.innerHTML = html;
  });
}

// Call this after creating victory screen
setTimeout(() => {
  loadPhotoAlbum();
}, 1000);
```

---

## 🎵 AUDIO FILES NEEDED

### **Blow Ball Audio (3 files):**
✅ `blowball_explainer.mp3` - YOU HAVE THIS
✅ `blowball_10sec.mp3` - YOU HAVE THIS (note: there's also "blowball_10sec..mp3" with double dots - fix filename)

### **Interview Round Audio:**

**MISSING - Need to create:**
❌ **interview_intro.mp3** - Host introduces the interview round
  - Script: "Time for the interview! Let's see what you've got to say!"
  - Duration: 3-4 seconds
  - Voice: Host (Clyde)

**MISSING - Need to create:**
❌ **interview_question_intro.mp3** - Before each question
  - Script: "Here's your question..."
  - Duration: 2-3 seconds
  - Voice: Host (Clyde)

**MISSING - Need to create:**
❌ **interview_voting_open.mp3** - When voting opens
  - Script: "Voting is open!"
  - Duration: 2 seconds
  - Voice: Host (Clyde)

**MISSING - Need to create (10 variations):**
❌ **interview_winner_1.mp3** through **interview_winner_10.mp3**
  - Scripts (rotate):
    1. "And the winner is..."
    2. "The votes are in, and the winner is..."
    3. "Topping the poll..."
    4. "And taking the victory..."
    5. "The answer everyone loved..."
    6. "Your winner..."
    7. "The crowd favorite..."
    8. "First place goes to..."
    9. "And the champion answer is..."
    10. "Stealing the show..."
  - Duration: 2-3 seconds each
  - Voice: Host (Clyde)

---

## 🔧 FIREBASE STRUCTURE

```javascript
{
  blowBall: {
    active: true,
    emotion: "😐 Serious",
    timeLeft: 10,
    photoRound: 1,
    photographerSelectionActive: true,
    photographers: {
      team1: "player1",
      team2: "player3"
    },
    photos: {
      player1: {
        photo1: {
          photo: "data:image/jpeg;base64,...",
          round: 1,
          timestamp: 1234567890
        }
      }
    },
    scores: {
      team1: 4,
      team2: 3
    },
    judgingActive: true,
    complete: true
  }
}
```

---

## ✅ TESTING CHECKLIST

**Part A - Interview Movement:**
- [ ] Round 2 ends → Interview Round starts
- [ ] Interview questions work
- [ ] Interview voting works
- [ ] Interview ends → Scores Review #3
- [ ] Scores Review #3 → Match Draw

**Part B - Blow Ball:**
- [ ] Goal Posts judging → Blow Ball starts
- [ ] Explainer shows
- [ ] Photographer selection works
- [ ] One player from each team can volunteer
- [ ] Emotions display (6 total)
- [ ] 10-second timer for each
- [ ] Photographers can take photos
- [ ] Non-photographers see emotion
- [ ] Photos upload to Firebase
- [ ] Referee can score both teams
- [ ] Points awarded correctly
- [ ] Goes to Scores Review #6
- [ ] Victory screen shows photo album

---

## ⏱️ TIME ESTIMATES

**Part A (Interview Move):** 10 minutes
**Part B (Blow Ball):** 45-60 minutes
**Total:** ~1 hour

---

## 🚀 SUMMARY

**Interview Round Changes:**
- Moves from position 6 to position 3
- Now happens after Round 2 (Puns)
- Scores Review #3 added after Interview
- All subsequent rounds shift down

**Blow Ball Implementation:**
- Camera-based photo capture
- 6 emotions × 10 seconds each
- Team photographers selected
- Photos uploaded to Firebase
- Referee scoring (1-5)
- Photo album in Victory Screen

**Audio Files Outstanding:**
- 4 Interview audio files needed (intro + variations)
- Blow Ball files already exist (check filename)

---

END OF BLOW BALL + INTERVIEW REPOSITIONING
Ready for Claude Code! 💨📸⚽✨
