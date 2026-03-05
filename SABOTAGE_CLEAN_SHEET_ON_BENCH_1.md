# CLAUDE CODE: IMPLEMENT SABOTAGE TASKS - CLEAN SHEET & ON THE BENCH
## Step-by-Step Implementation Instructions

---

## 🎯 OBJECTIVE

Implement the two initial sabotage tasks that are assigned when players get toilet paper:
1. **Clean Sheet** - Collect toilet paper pieces in pockets
2. **On The Bench** - Hide toilet paper pieces in a hiding place
S
These are SECRET tasks shown only to the assigned players. Players earn 1 point per piece if not caught.

---

## 📊 CURRENT STATE

**Location in game flow:**
```
Toilet Paper Alert → Sabotage Assignment → Bog Rolling → Goal Posts → Blow Ball
```

**Current implementation:**
- ✅ Toilet paper alert exists
- ✅ Basic sabotage assignment exists
- ❌ Tasks are incomplete/incorrect
- ❌ Need to update task descriptions
- ❌ Need to add completion tracking
- ❌ Need to add reveals at end

---

## 📝 STEP 1: UPDATE SABOTAGE TASK ASSIGNMENT

**File:** `host-complete_42.html`
**Location:** Find the `assignSabotageTasks()` function (around line 4100)

**Current code looks like:**
```javascript
function assignSabotageTasks() {
  console.log('🕵️ Assigning sabotage tasks');
  
  const team1Players = Object.keys(players).filter(pid => players[pid].team === 1);
  const team2Players = Object.keys(players).filter(pid => players[pid].team === 2);
  
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
```

**Replace with this COMPLETE version:**

```javascript
function assignSabotageTasks() {
  console.log('🕵️ Assigning initial sabotage tasks');
  
  const team1Players = Object.keys(players).filter(pid => players[pid].team === 1);
  const team2Players = Object.keys(players).filter(pid => players[pid].team === 2);
  
  // Task definitions
  const sabotageTaskDefinitions = {
    clean_sheet: {
      id: 'clean_sheet',
      name: 'Clean Sheet',
      description: 'Put as many pieces of toilet paper in your pocket as possible. You may only pick up pieces off the floor and each piece must be separated. You will get one point per piece at the end of the game if nobody has spotted you. Tell no one.',
      pointsPerPiece: 1
    },
    on_bench: {
      id: 'on_bench',
      name: 'On The Bench',
      description: 'Choose a hiding place and stash as many pieces of toilet paper as possible there. You may only pick pieces up off the floor, and each piece must be separated. You will get one point per piece at the end of the game if nobody has spotted you. Tell no one.',
      pointsPerPiece: 1
    }
  };
  
  // Assign Clean Sheet to random Team 1 player
  if (team1Players.length > 0) {
    const randomPlayer1 = team1Players[Math.floor(Math.random() * team1Players.length)];
    const task = sabotageTaskDefinitions.clean_sheet;
    
    gameRef.child(`sabotage/${randomPlayer1}`).set({
      task: task.id,
      name: task.name,
      description: task.description,
      pointsPerPiece: task.pointsPerPiece,
      assigned: true,
      completed: false,
      piecesCollected: 0,
      points: 0
    });
    
    console.log(`🕵️ Assigned Clean Sheet to ${players[randomPlayer1].name}`);
  }
  
  // Assign On The Bench to random Team 2 player
  if (team2Players.length > 0) {
    const randomPlayer2 = team2Players[Math.floor(Math.random() * team2Players.length)];
    const task = sabotageTaskDefinitions.on_bench;
    
    gameRef.child(`sabotage/${randomPlayer2}`).set({
      task: task.id,
      name: task.name,
      description: task.description,
      pointsPerPiece: task.pointsPerPiece,
      assigned: true,
      completed: false,
      piecesCollected: 0,
      points: 0
    });
    
    console.log(`🕵️ Assigned On The Bench to ${players[randomPlayer2].name}`);
  }
}
```

---

## 📝 STEP 2: UPDATE PLAYER SABOTAGE DISPLAY

**File:** `player-complete_27.html`
**Location:** Find the `showSabotageTask()` function (around line 1400 or search for "showSabotageTask")

**Current code might look like:**
```javascript
function showSabotageTask(sabotageData) {
  const alertDiv = document.getElementById('player-tp-alert');
  if (alertDiv) {
    alertDiv.innerHTML += `
      <div style="...">
        ${sabotageData.name}
        ${sabotageData.description}
      </div>
    `;
  }
}
```

**Replace with this COMPLETE version:**

```javascript
function showSabotageTask(sabotageData) {
  console.log('🕵️ Showing sabotage task:', sabotageData.name);
  
  const alertDiv = document.getElementById('player-tp-alert');
  if (!alertDiv) {
    // If alert div gone, create standalone sabotage display
    createStandaloneSabotageDisplay(sabotageData);
    return;
  }
  
  // Add sabotage task to toilet paper alert
  const sabotageHTML = `
    <div id="sabotage-task-display" style="margin-top: 40px; padding: 30px; background: rgba(212,20,90,0.3); border: 2px solid #d4145a; border-radius: 15px; max-width: 600px;">
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 32px; color: #d4145a; margin-bottom: 15px;">
        🕵️ SECRET SABOTAGE MISSION
      </div>
      
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 24px; color: #fff; margin-bottom: 10px;">
        ${sabotageData.name}
      </div>
      
      <div style="font-family: 'Barlow', sans-serif; font-size: 18px; color: rgba(255,255,255,0.9); margin-bottom: 20px; line-height: 1.6;">
        ${sabotageData.description}
      </div>
      
      <div style="font-family: 'Barlow', sans-serif; font-size: 16px; color: rgba(255,255,255,0.7); margin-bottom: 20px; font-style: italic;">
        ${sabotageData.pointsPerPiece} point per piece!<br>
        Complete this WITHOUT getting caught!
      </div>
      
      <button onclick="acknowledgeSabotage()" 
              style="width: 100%; padding: 15px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 12px; font-family: 'Bebas Neue', sans-serif; font-size: 24px; cursor: pointer; box-shadow: 0 8px 20px rgba(77,212,232,0.4);">
        Understood
      </button>
    </div>
  `;
  
  alertDiv.innerHTML += sabotageHTML;
}

function createStandaloneSabotageDisplay(sabotageData) {
  // If toilet paper alert is gone, create standalone display
  const sabotageDiv = document.createElement('div');
  sabotageDiv.id = 'standalone-sabotage';
  sabotageDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, #0a1628 0%, #1a2b4a 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10000; padding: 30px; text-align: center;';
  sabotageDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 48px; color: #d4145a; margin-bottom: 30px;">
      🕵️ SECRET MISSION
    </div>
    
    <div style="max-width: 600px; padding: 30px; background: rgba(212,20,90,0.3); border: 2px solid #d4145a; border-radius: 15px;">
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 28px; color: #fff; margin-bottom: 15px;">
        ${sabotageData.name}
      </div>
      
      <div style="font-family: 'Barlow', sans-serif; font-size: 18px; color: rgba(255,255,255,0.9); margin-bottom: 20px; line-height: 1.6;">
        ${sabotageData.description}
      </div>
      
      <div style="font-family: 'Barlow', sans-serif; font-size: 16px; color: rgba(255,255,255,0.7); margin-bottom: 25px; font-style: italic;">
        ${sabotageData.pointsPerPiece} point per piece!
      </div>
      
      <button onclick="acknowledgeSabotage()" 
              style="width: 100%; padding: 15px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 12px; font-family: 'Bebas Neue', sans-serif; font-size: 24px; cursor: pointer;">
        Understood
      </button>
    </div>
  `;
  
  document.body.appendChild(sabotageDiv);
}

function acknowledgeSabotage() {
  console.log('✅ Sabotage task acknowledged');
  
  // Remove sabotage display
  const taskDisplay = document.getElementById('sabotage-task-display');
  if (taskDisplay) taskDisplay.remove();
  
  const standaloneDisplay = document.getElementById('standalone-sabotage');
  if (standaloneDisplay) standaloneDisplay.remove();
  
  // Show persistent reminder
  showSabotageReminder();
}

function showSabotageReminder() {
  // Create small persistent reminder at bottom of screen
  const reminderDiv = document.createElement('div');
  reminderDiv.id = 'sabotage-reminder';
  reminderDiv.style.cssText = 'position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: rgba(212,20,90,0.9); padding: 12px 24px; border-radius: 8px; z-index: 9999; box-shadow: 0 4px 12px rgba(0,0,0,0.4);';
  reminderDiv.innerHTML = `
    <div style="font-family: 'Barlow', sans-serif; font-size: 14px; color: white; display: flex; align-items: center; gap: 10px;">
      <span style="font-size: 18px;">🕵️</span>
      <span>Secret Mission Active</span>
      <button onclick="viewSabotageDetails()" 
              style="margin-left: 10px; padding: 4px 12px; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.4); border-radius: 4px; color: white; font-size: 12px; cursor: pointer;">
        View
      </button>
    </div>
  `;
  
  document.body.appendChild(reminderDiv);
}

function viewSabotageDetails() {
  // Fetch and show sabotage task details again
  gameRef.child(`sabotage/${playerId}`).once('value', (snapshot) => {
    const sabotageData = snapshot.val();
    if (sabotageData) {
      createStandaloneSabotageDisplay(sabotageData);
    }
  });
}
```

---

## 📝 STEP 3: ADD SABOTAGE COMPLETION TRACKING

**File:** `player-complete_27.html`
**Location:** Add after the sabotage display functions

**Add these NEW functions:**

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// SABOTAGE COMPLETION TRACKING
// ═══════════════════════════════════════════════════════════════════════════

function markSabotageInProgress() {
  // Player indicates they're working on their sabotage
  gameRef.child(`sabotage/${playerId}`).update({
    inProgress: true,
    startedAt: Date.now()
  });
  
  console.log('🕵️ Sabotage marked as in progress');
}

function updateSabotagePieces(pieces) {
  // Update how many pieces collected
  gameRef.child(`sabotage/${playerId}`).update({
    piecesCollected: pieces
  });
  
  console.log(`🕵️ Updated sabotage pieces: ${pieces}`);
}

function markSabotageComplete(pieces) {
  // Mark task as complete with final piece count
  gameRef.child(`sabotage/${playerId}`).update({
    completed: true,
    piecesCollected: pieces,
    points: pieces, // 1 point per piece
    completedAt: Date.now()
  });
  
  console.log(`✅ Sabotage complete: ${pieces} pieces`);
  
  // Show confirmation
  const confirmDiv = document.createElement('div');
  confirmDiv.style.cssText = 'position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(77,212,232,0.95); padding: 30px; border-radius: 15px; z-index: 11000; box-shadow: 0 10px 30px rgba(0,0,0,0.5);';
  confirmDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 32px; color: #0a1628; margin-bottom: 15px; text-align: center;">
      ✅ Mission Complete!
    </div>
    <div style="font-family: 'Barlow', sans-serif; font-size: 18px; color: #0a1628; text-align: center;">
      ${pieces} pieces collected<br>
      Worth ${pieces} points if not caught!
    </div>
  `;
  
  document.body.appendChild(confirmDiv);
  
  setTimeout(() => {
    confirmDiv.remove();
  }, 3000);
}

function reportSabotageSpotted(spottedPlayerId) {
  // Player reports seeing someone else's sabotage
  gameRef.child(`sabotage/${spottedPlayerId}`).update({
    spotted: true,
    spottedBy: playerId,
    spottedAt: Date.now(),
    points: 0 // No points if caught!
  });
  
  console.log(`🚨 Reported sabotage by ${spottedPlayerId}`);
}
```

---

## 📝 STEP 4: ADD SABOTAGE SELF-REPORTING INTERFACE

**File:** `player-complete_27.html`
**Location:** Add after the completion tracking functions

**Add this NEW function:**

```javascript
function showSabotageCompletionInterface() {
  const interfaceDiv = document.createElement('div');
  interfaceDiv.id = 'sabotage-completion-interface';
  interfaceDiv.style.cssText = 'position: fixed; bottom: 80px; right: 20px; background: rgba(212,20,90,0.95); padding: 20px; border-radius: 12px; z-index: 9999; box-shadow: 0 8px 20px rgba(0,0,0,0.5); max-width: 300px;';
  interfaceDiv.innerHTML = `
    <div style="font-family: 'Bebas Neue', sans-serif; font-size: 20px; color: white; margin-bottom: 15px;">
      🕵️ Report Progress
    </div>
    
    <div style="font-family: 'Barlow', sans-serif; font-size: 14px; color: rgba(255,255,255,0.9); margin-bottom: 15px;">
      How many pieces have you collected?
    </div>
    
    <input type="number" 
           id="sabotage-pieces-input" 
           min="0" 
           max="100"
           placeholder="Number of pieces"
           style="width: 100%; padding: 10px; border: none; border-radius: 6px; font-size: 16px; margin-bottom: 12px;">
    
    <div style="display: flex; gap: 10px;">
      <button onclick="submitSabotagePieces()" 
              style="flex: 1; padding: 10px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 6px; font-family: 'Bebas Neue', sans-serif; font-size: 16px; cursor: pointer;">
        Submit
      </button>
      <button onclick="closeSabotageInterface()" 
              style="padding: 10px 15px; background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.4); border-radius: 6px; font-size: 14px; cursor: pointer;">
        Cancel
      </button>
    </div>
  `;
  
  document.body.appendChild(interfaceDiv);
}

function submitSabotagePieces() {
  const input = document.getElementById('sabotage-pieces-input');
  const pieces = parseInt(input.value) || 0;
  
  if (pieces < 0) {
    alert('Please enter a valid number of pieces');
    return;
  }
  
  markSabotageComplete(pieces);
  closeSabotageInterface();
  
  // Remove the reminder
  const reminder = document.getElementById('sabotage-reminder');
  if (reminder) reminder.remove();
}

function closeSabotageInterface() {
  const interfaceDiv = document.getElementById('sabotage-completion-interface');
  if (interfaceDiv) interfaceDiv.remove();
}
```

---

## 📝 STEP 5: UPDATE SABOTAGE REMINDER TO INCLUDE REPORTING

**File:** `player-complete_27.html`
**Location:** Update the `showSabotageReminder()` function created in Step 2

**Replace the existing reminder with:**

```javascript
function showSabotageReminder() {
  // Create small persistent reminder at bottom of screen
  const reminderDiv = document.createElement('div');
  reminderDiv.id = 'sabotage-reminder';
  reminderDiv.style.cssText = 'position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: rgba(212,20,90,0.9); padding: 12px 24px; border-radius: 8px; z-index: 9999; box-shadow: 0 4px 12px rgba(0,0,0,0.4);';
  reminderDiv.innerHTML = `
    <div style="font-family: 'Barlow', sans-serif; font-size: 14px; color: white; display: flex; align-items: center; gap: 10px;">
      <span style="font-size: 18px;">🕵️</span>
      <span>Secret Mission Active</span>
      <button onclick="viewSabotageDetails()" 
              style="margin-left: 10px; padding: 4px 12px; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.4); border-radius: 4px; color: white; font-size: 12px; cursor: pointer;">
        View
      </button>
      <button onclick="showSabotageCompletionInterface()" 
              style="margin-left: 5px; padding: 4px 12px; background: rgba(77,212,232,0.3); border: 1px solid rgba(77,212,232,0.6); border-radius: 4px; color: white; font-size: 12px; cursor: pointer;">
        Report
      </button>
    </div>
  `;
  
  document.body.appendChild(reminderDiv);
}
```

---

## 📝 STEP 6: ADD SABOTAGE REVEAL SCREEN (HOST)

**File:** `host-complete_42.html`
**Location:** After Interview Round ends, before Victory Screen (around line 3500 or search for "showVictoryScreen")

**Find where Interview Round ends and Victory Screen starts. Add this BEFORE Victory Screen:**

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// SABOTAGE REVEALS
// ═══════════════════════════════════════════════════════════════════════════

function showSabotageReveals() {
  console.log('🕵️ Showing Sabotage Reveals');
  
  // Get all sabotage tasks
  gameRef.child('sabotage').once('value', (snapshot) => {
    const sabotageData = snapshot.val();
    
    if (!sabotageData || Object.keys(sabotageData).length === 0) {
      // No sabotage tasks, go straight to victory
      showVictoryScreen();
      return;
    }
    
    const revealDiv = document.createElement('div');
    revealDiv.id = 'sabotage-reveals';
    revealDiv.style.cssText = 'position: fixed; inset: 0; background: linear-gradient(135deg, var(--motd-dark-navy) 0%, var(--motd-navy) 100%); display: flex; flex-direction: column; align-items: center; padding: 40px; overflow-y: auto; z-index: 10000;';
    
    let html = `
      <div style="font-family: 'Bebas Neue', sans-serif; font-size: 72px; color: var(--motd-gold); text-shadow: 0 0 40px rgba(255,198,41,0.8); margin-bottom: 40px; letter-spacing: 6px;">
        🕵️ SABOTAGE REVEALS
      </div>
      
      <div style="font-family: 'Oswald', sans-serif; font-size: 32px; color: var(--text); margin-bottom: 50px; text-align: center;">
        Some players had secret missions...
      </div>
      
      <div style="display: flex; flex-direction: column; gap: 30px; width: 100%; max-width: 800px;">
    `;
    
    Object.entries(sabotageData).forEach(([playerId, data]) => {
      const playerName = players[playerId]?.name || 'Unknown';
      const completed = data.completed || false;
      const spotted = data.spotted || false;
      const pieces = data.piecesCollected || 0;
      
      let statusText = '';
      let statusColor = '';
      let points = 0;
      
      if (spotted) {
        statusText = '🚨 CAUGHT!';
        statusColor = '#d4145a';
        points = 0;
      } else if (completed) {
        statusText = '✅ COMPLETED';
        statusColor = '#4dd4e8';
        points = pieces; // 1 point per piece
      } else {
        statusText = '❌ NOT COMPLETED';
        statusColor = '#666';
        points = 0;
      }
      
      html += `
        <div style="background: rgba(212,20,90,0.2); border: 2px solid #d4145a; border-radius: 15px; padding: 30px;">
          <div style="font-family: 'Bebas Neue', sans-serif; font-size: 36px; color: #fff; margin-bottom: 15px;">
            ${playerName}
          </div>
          
          <div style="font-family: 'Bebas Neue', sans-serif; font-size: 24px; color: #d4145a; margin-bottom: 10px;">
            Mission: ${data.name}
          </div>
          
          <div style="font-family: 'Barlow', sans-serif; font-size: 18px; color: rgba(255,255,255,0.8); margin-bottom: 20px;">
            ${data.description}
          </div>
          
          ${pieces > 0 ? `
            <div style="font-family: 'Barlow', sans-serif; font-size: 20px; color: rgba(255,255,255,0.9); margin-bottom: 15px;">
              📊 Collected: ${pieces} pieces
            </div>
          ` : ''}
          
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-family: 'Bebas Neue', sans-serif; font-size: 28px; color: ${statusColor};">
              ${statusText}
            </div>
            
            <div style="font-family: 'Bebas Neue', sans-serif; font-size: 36px; color: #ffc629;">
              +${points} points
            </div>
          </div>
        </div>
      `;
    });
    
    html += `
      </div>
      
      <button onclick="finishSabotageReveals()" 
              style="margin-top: 50px; padding: 20px 50px; background: linear-gradient(135deg, #4dd4e8, #ffc629); color: #0a1628; border: none; border-radius: 15px; font-family: 'Bebas Neue', sans-serif; font-size: 32px; cursor: pointer; box-shadow: 0 10px 30px rgba(255,198,41,0.4);">
        Continue to Results
      </button>
    `;
    
    revealDiv.innerHTML = html;
    document.body.appendChild(revealDiv);
    
    // Award sabotage points
    Object.entries(sabotageData).forEach(([playerId, data]) => {
      if (data.completed && !data.spotted) {
        const points = data.piecesCollected || 0;
        gameRef.child(`players/${playerId}/score`).transaction((current) => {
          return (current || 0) + points;
        });
        console.log(`✅ Awarded ${points} sabotage points to ${players[playerId]?.name}`);
      }
    });
  });
}

function finishSabotageReveals() {
  const revealDiv = document.getElementById('sabotage-reveals');
  if (revealDiv) revealDiv.remove();
  
  showVictoryScreen();
}
```

---

## 📝 STEP 7: UPDATE INTERVIEW ROUND TO GO TO SABOTAGE REVEALS

**File:** `host-complete_42.html`
**Location:** Find where Interview Round ends (search for "nextRound3Question" or around line 3110)

**Find this code:**
```javascript
function nextRound3Question() {
  round3CurrentQ++;
  if (round3CurrentQ < ROUND_3_QUESTIONS.length) {
    loadRound3Question(round3CurrentQ);
  } else {
    // Round 3 (Interview) complete → Victory Screen
    showVictoryScreen();
  }
}
```

**Change to:**
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

---

## 🎯 FIREBASE STRUCTURE

The code creates this structure:

```javascript
{
  sabotage: {
    player1: {
      task: "clean_sheet",
      name: "Clean Sheet",
      description: "Put as many pieces of toilet paper...",
      pointsPerPiece: 1,
      assigned: true,
      completed: true,
      piecesCollected: 15,
      points: 15,
      spotted: false,
      inProgress: true,
      startedAt: 1234567890,
      completedAt: 1234567899
    },
    player2: {
      task: "on_bench",
      name: "On The Bench",
      description: "Choose a hiding place...",
      pointsPerPiece: 1,
      assigned: true,
      completed: true,
      piecesCollected: 22,
      points: 22,
      spotted: false
    }
  }
}
```

---

## ✅ TESTING CHECKLIST

After implementation:

**Sabotage Assignment:**
- [ ] Toilet paper alert shows
- [ ] Random Team 1 player gets "Clean Sheet"
- [ ] Random Team 2 player gets "On The Bench"
- [ ] Task shows with correct description
- [ ] "Understood" button works
- [ ] Reminder appears at bottom

**During Game:**
- [ ] Reminder stays visible
- [ ] "View" button shows task again
- [ ] "Report" button opens interface
- [ ] Can enter number of pieces
- [ ] Submit button works
- [ ] Confirmation shows

**Sabotage Reveals:**
- [ ] Shows after Interview Round
- [ ] Lists all sabotage tasks
- [ ] Shows player names
- [ ] Shows pieces collected
- [ ] Shows completed/not completed status
- [ ] Awards correct points
- [ ] "Continue" goes to Victory Screen

---

## 📊 POINTS SYSTEM

**Clean Sheet:**
- 1 point per piece of toilet paper
- Only if NOT caught/spotted
- Self-reported by player

**On The Bench:**
- 1 point per piece of toilet paper
- Only if NOT caught/spotted
- Self-reported by player

**If Spotted:**
- 0 points
- Shows "CAUGHT" in red
- No points awarded

---

## 🎨 UI FEATURES

### **Player Sabotage Display:**
- Large red bordered box
- Secret mission styling
- Clear description
- Point value shown
- "Understood" button

### **Persistent Reminder:**
- Small badge at bottom center
- Shows "Secret Mission Active"
- Two buttons: "View" and "Report"
- Stays visible throughout game

### **Completion Interface:**
- Floating box bottom right
- Number input for pieces
- Submit and Cancel buttons
- Confirmation message

### **Reveal Screen:**
- Full screen display
- Shows all players' tasks
- Status indicators (✅/❌/🚨)
- Points awarded
- Professional styling

---

## ⚠️ IMPORTANT NOTES

### **Self-Reporting System:**
- Players report their own pieces
- Honor system (no verification)
- Can be caught by other players (future feature)

### **Timing:**
- Tasks assigned at toilet paper alert
- Can be completed anytime during toilet paper rounds
- Revealed after Interview Round
- Points awarded before Victory Screen

### **No Verification:**
- Game doesn't verify pieces collected
- Relies on honesty
- Social pressure prevents cheating

---

## 🚀 SUMMARY

**What gets added:**
- Updated sabotage assignment with full task definitions
- Player sabotage display with persistent reminder
- Self-reporting interface for completion
- Host sabotage reveal screen
- Points calculation and award system

**Time estimate:** 20-30 minutes

**Complexity:** LOW-MEDIUM

**Dependencies:**
- Existing toilet paper alert
- Existing Interview Round
- Existing Victory Screen

---

## 📋 IMPLEMENTATION ORDER

1. Update `assignSabotageTasks()` in host file (Step 1)
2. Update player sabotage display (Step 2)
3. Add completion tracking functions (Step 3)
4. Add completion interface (Step 4)
5. Update reminder with report button (Step 5)
6. Add sabotage reveals screen (Step 6)
7. Update Interview end to show reveals (Step 7)
8. Test with 2+ players

---

END OF CLEAN SHEET & ON THE BENCH IMPLEMENTATION
Ready for Claude Code! 🕵️⚽✨
