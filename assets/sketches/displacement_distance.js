// 位移与路程动画演示
// 位移：矢量，可正可负
// 路程：标量，只增不减

let t = 0;           // 时间
let x0 = 150;        // 起始位置
let x = x0;          // 当前位置
let direction = 1;   // 运动方向 (1: 右, -1: 左)
let speed = 2;       // 速度
let maxFrames = 240; // 最大帧数（10秒 * 30帧/秒）
let isRunning = true; // 动画是否运行中

// 记录数据用于绘图
let displacementData = [];  // 位移数据
let distanceData = [];       // 路程数据
let totalDistance = 0;       // 累计路程

function setup() {
  createCanvas(700, 350);
  frameRate(30);
  textFont('Arial');
}

function draw() {
  background(245);
  
  // ========== 左侧：物体运动区域 ==========
  push();
  
  // 标题
  fill(50);
  textSize(12);
  textAlign(CENTER);
  text("物体运动", 150, 20);
  
  // 绘制运动轨道
  stroke(180);
  strokeWeight(2);
  line(30, 150, 270, 150);
  
  // 绘制刻度
  for (let i = 0; i <= 6; i++) {
    let px = 30 + i * 40;
    line(px, 145, px, 155);
    textSize(10);
    fill(100);
    noStroke();
    textAlign(CENTER);
    text((i - 3) * 40, px, 170);
  }
  
  // 绘制原点标记
  stroke(0, 150, 0);
  strokeWeight(2);
  line(x0, 130, x0, 170);
  noStroke();
  fill(0, 150, 0);
  textSize(10);
  text("O", x0, 125);
  
  // 绘制物体（方块）
  fill(220, 80, 60);
  noStroke();
  rectMode(CENTER);
  rect(x, 150, 20, 20, 3);
  
  // 绘制位移箭头
  if (abs(x - x0) > 5) {
    stroke(0, 100, 200);
    strokeWeight(2);
    drawArrow(x0, 190, x, 190);
    noStroke();
    fill(0, 100, 200);
    textSize(10);
    let disp = x - x0;
    text("位移: " + (disp > 0 ? "+" : "") + disp.toFixed(0), (x0 + x) / 2, 210);
  }
  
  pop();
  
  // ========== 右上：位移-时间图 ==========
  push();
  translate(320, 20);
  drawGraph("位移 s (矢量)", displacementData, color(0, 100, 200), true);
  pop();
  
  // ========== 右下：路程-时间图 ==========
  push();
  translate(320, 185);
  drawGraph("路程 d (标量)", distanceData, color(220, 120, 0), false);
  pop();
  
  // ========== 显示状态提示 ==========
  if (!isRunning) {
    push();
    fill(0, 0, 0, 100);
    rect(0, 0, 700, 350);
    fill(255);
    textSize(16);
    textAlign(CENTER, CENTER);
    text("演示结束 - 点击画面重播", 350, 175);
    pop();
  }
  
  // ========== 更新物理状态 ==========
  if (isRunning) {
    updatePhysics();
  }
}

// 绘制坐标系和曲线
function drawGraph(title, data, lineColor, showNegative) {
  let w = 350;
  let h = 140;
  
  // 背景
  fill(255);
  stroke(200);
  strokeWeight(1);
  rect(0, 0, w, h, 5);
  
  // 标题
  noStroke();
  fill(50);
  textSize(11);
  textAlign(LEFT);
  text(title, 10, 18);
  
  // 坐标系
  let ox = 40;
  let oy = showNegative ? h / 2 : h - 25;
  let graphW = w - 60;
  let graphH = showNegative ? (h - 50) / 2 : h - 45;
  
  stroke(150);
  strokeWeight(1);
  // x轴（时间轴）
  line(ox, oy, ox + graphW, oy);
  // y轴
  line(ox, showNegative ? 25 : (h - 25), ox, showNegative ? (h - 25) : 25);
  
  // 轴标签
  noStroke();
  fill(100);
  textSize(9);
  textAlign(CENTER);
  text("t", ox + graphW + 10, oy + 4);
  textAlign(RIGHT);
  text("0", ox - 5, oy + 4);
  
  // 时间刻度（0s, 5s, 10s）
  textSize(8);
  textAlign(CENTER);
  text("5s", ox + graphW / 2, oy + 12);
  text("10s", ox + graphW, oy + 12);
  
  if (showNegative) {
    textAlign(RIGHT);
    text("+", ox - 5, 35);
    text("-", ox - 5, h - 30);
  } else {
    textAlign(RIGHT);
    text("+", ox - 5, 35);
  }
  
  // 绘制数据曲线
  if (data.length > 1) {
    stroke(lineColor);
    strokeWeight(2);
    noFill();
    beginShape();
    for (let i = 0; i < data.length; i++) {
      let px = ox + (i / 300) * graphW;  // 使用 maxFrames (300) 作为基准
      let py;
      if (showNegative) {
        py = oy - (data[i] / 120) * graphH;  // 调整缩放比例
      } else {
        py = oy - (data[i] / 600) * graphH;  // 调整缩放比例
      }
      py = constrain(py, 25, h - 25);
      vertex(px, py);
    }
    endShape();
  }
  
  // 当前值
  if (data.length > 0) {
    let val = data[data.length - 1];
    noStroke();
    fill(lineColor);
    textSize(10);
    textAlign(RIGHT);
    let valStr = showNegative ? ((val >= 0 ? "+" : "") + val.toFixed(0)) : val.toFixed(0);
    text(valStr, w - 15, 18);
  }
}

// 绘制箭头
function drawArrow(x1, y1, x2, y2) {
  line(x1, y1, x2, y2);
  let angle = atan2(y2 - y1, x2 - x1);
  let arrowSize = 6;
  push();
  translate(x2, y2);
  rotate(angle);
  line(0, 0, -arrowSize, -arrowSize / 2);
  line(0, 0, -arrowSize, arrowSize / 2);
  pop();
}

// 更新物理状态
function updatePhysics() {
  // 检查是否达到最大时间
  if (t >= maxFrames) {
    isRunning = false;
    return;
  }
  
  // 更新位置
  x += direction * speed;
  
  // 边界反弹
  if (x > 260) {
    x = 260;
    direction = -1;
  }
  if (x < 40) {
    x = 40;
    direction = 1;
  }
  
  // 计算位移（相对于起点，有正负）
  let displacement = x - x0;
  
  // 计算路程（累计，只增不减）
  totalDistance += speed;
  
  // 记录数据
  displacementData.push(displacement);
  distanceData.push(totalDistance);
  
  // 限制数据长度（只在不超过最大帧数时限制）
  if (displacementData.length > maxFrames) {
    displacementData.shift();
    distanceData.shift();
  }
  
  t++;
}

// 点击重置并重播
function mousePressed() {
  if (mouseX > 0 && mouseX < 700 && mouseY > 0 && mouseY < 350) {
    // 重置所有状态
    t = 0;
    x = x0;
    direction = 1;
    totalDistance = 0;
    displacementData = [];
    distanceData = [];
    isRunning = true;  // 重新开始播放
  }
}
