const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Game Variables
const player = {
  x: canvas.width / 2,
  y: canvas.height / 2,
  width: 50,
  height: 50,
  speed: 2,
  dx: 0,
  dy: 0
};

const goal = {
    x: canvas.width - 60,  // Positioned near the bottom-right corner
    y: canvas.height - 60,
    width: 50,
    height: 50,
    color: 'green'
  };

// Input Listeners
document.addEventListener('keydown', keyDown);
document.addEventListener('keyup', keyUp);

// Update Game
function update() {
  player.x += player.dx;
  player.y += player.dy;

  detectWallCollision();
  checkGoalCollision();

  clear();
  drawPlayer();
  drawGoal();
  
  requestAnimationFrame(update);
}

// Detect collision with walls
function detectWallCollision() {
  if (player.x < 0) player.x = 0;
  if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
  if (player.y < 0) player.y = 0;
  if (player.y + player.height > canvas.height) player.y = canvas.height - player.height;
}

// Check if player reaches the goal
function checkGoalCollision() {
    if (player.x < goal.x + goal.width &&
        player.x + player.width > goal.x &&
        player.y < goal.y + goal.height &&
        player.y + player.height > goal.y) {
      alert("You reached the goal!");
      resetGame();
    }
  }

// Draw Player
function drawPlayer() {
  ctx.fillStyle = 'blue';
  ctx.fillRect(player.x, player.y, player.width, player.height);
}

// Draw Goal
function drawGoal() {
    ctx.fillStyle = goal.color;
    ctx.fillRect(goal.x, goal.y, goal.width, goal.height);
  }

// Clear canvas
function clear() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Reset the game (player goes back to starting position)
function resetGame() {
    player.x = canvas.width / 2;
    player.y = canvas.height / 2;
  }

// Move Player
function movePlayer(dx, dy) {
  player.dx = dx;
  player.dy = dy;
}

// Handle Key Press
function keyDown(e) {
  switch(e.key) {
    case 'ArrowRight':
    case 'd':
      movePlayer(player.speed, 0);
      break;
    case 'ArrowLeft':
    case 'a':
      movePlayer(-player.speed, 0);
      break;
    case 'ArrowUp':
    case 'w':
      movePlayer(0, -player.speed);
      break;
    case 'ArrowDown':
    case 's':
      movePlayer(0, player.speed);
      break;
  }
}

// Handle Key Release
function keyUp(e) {
  switch(e.key) {
    case 'ArrowRight':
    case 'd':
    case 'ArrowLeft':
    case 'a':
      movePlayer(0, 0);
      break;
    case 'ArrowUp':
    case 'w':
    case 'ArrowDown':
    case 's':
      movePlayer(0, 0);
      break;
  }
}

// Start Game
update();
