// 速度与加速度动画演示
// 演示 v 和 a 的关系，以及 v-t 图像

let x = 100;          // 小车位置
let v = 0;            // 速度
let a = 0;            // 加速度
let t = 0;            // 时间

let aSlider;          // 加速度滑块
let velocityData = []; // 速度-时间数据
let maxDataPoints = 300; // 最大数据点数（10秒）

function setup() {
  createCanvas(700, 420);
  frameRate(30);
  textFont('Arial');
  
  // 创建加速度滑块
  aSlider = createSlider(-3, 3, 0, 0.1);
  aSlider.position(10, 10);
  aSlider.size(150);
}

function draw() {
  background(245);
  
  // 获取滑块值
  a = aSlider.value();
  
  // ========== 顶部：控制区域 ==========
  drawControlPanel();
  
  // ========== 中部：小车运动区域 ==========
  drawCarArea();
  
  // ========== 底部：v-t 图像 ==========
  push();
  translate(20, 230);
  drawVTGraph();
  pop();
  
  // ========== 更新物理状态 ==========
  updatePhysics();
}

// 绘制控制面板
function drawControlPanel() {
  push();
  fill(50);
  textSize(12);
  textAlign(LEFT);
  text("加速度 a:", 10, 50);
  
  // 显示加速度数值
  let aText = a.toFixed(1) + " m/s²";
  if (a > 0) aText = "+" + aText;
  fill(a === 0 ? 100 : (a > 0 ? 0 : 200), a === 0 ? 100 : 0, a === 0 ? 100 : (a < 0 ? 0 : 200));
  textSize(14);
  text(aText, 170, 25);
  
  // 重置按钮提示
  fill(100);
  textSize(10);
  text("点击画面重置", 620, 20);
  pop();
}

// 绘制小车运动区域
function drawCarArea() {
  push();
  translate(0, 60);
  
  // 背景区域
  fill(255);
  stroke(200);
  rect(10, 10, 680, 150, 5);
  
  // 绘制地面
  stroke(150);
  strokeWeight(2);
  line(30, 120, 670, 120);
  
  // 绘制刻度
  strokeWeight(1);
  for (let i = 0; i <= 12; i++) {
    let px = 50 + i * 50;
    line(px, 115, px, 125);
  }
  
  // 判断加速还是减速
  let isAccelerating = (v * a > 0) || (v === 0 && a !== 0);
  let isDecelerating = (v * a < 0);
  
  // 绘制小车
  push();
  translate(x, 100);
  
  // 车身颜色
  if (isAccelerating) {
    fill(80, 180, 80);  // 绿色 - 加速
  } else if (isDecelerating) {
    fill(220, 80, 80);  // 红色 - 减速
  } else {
    fill(100, 100, 100);  // 灰色 - 匀速
  }
  
  noStroke();
  rectMode(CENTER);
  rect(0, 0, 50, 25, 5);
  
  // 车轮
  fill(50);
  ellipse(-15, 12, 12, 12);
  ellipse(15, 12, 12, 12);
  
  pop();
  
  // 绘制速度箭头（绿色）
  if (abs(v) > 0.1) {
    push();
    translate(x, 65);
    stroke(0, 150, 0);
    strokeWeight(3);
    let vArrowLen = constrain(v * 15, -80, 80);
    drawArrow(0, 0, vArrowLen, 0);
    
    // 速度标签
    noStroke();
    fill(0, 150, 0);
    textSize(11);
    textAlign(CENTER);
    text("v = " + v.toFixed(1), vArrowLen / 2, -10);
    pop();
  }
  
  // 绘制加速度箭头（红色）
  if (abs(a) > 0.05) {
    push();
    translate(x, 45);
    stroke(200, 50, 50);
    strokeWeight(3);
    let aArrowLen = a * 20;
    drawArrow(0, 0, aArrowLen, 0);
    
    // 加速度标签
    noStroke();
    fill(200, 50, 50);
    textSize(11);
    textAlign(CENTER);
    text("a = " + a.toFixed(1), aArrowLen / 2, -10);
    pop();
  }
  
  // 状态提示
  fill(50);
  textSize(12);
  textAlign(LEFT);
  noStroke();
  let statusText = "";
  if (isAccelerating) {
    fill(80, 180, 80);
    statusText = "加速中 (v 与 a 同向)";
  } else if (isDecelerating) {
    fill(220, 80, 80);
    statusText = "减速中 (v 与 a 反向)";
  } else if (abs(v) < 0.1 && abs(a) < 0.05) {
    fill(100);
    statusText = "静止";
  } else {
    fill(100);
    statusText = "匀速运动";
  }
  text(statusText, 500, 25);
  
  pop();
}

// 绘制 v-t 图像
function drawVTGraph() {
  let w = 660;
  let h = 160;
  
  // 背景
  fill(255);
  stroke(200);
  strokeWeight(1);
  rect(0, 0, w, h, 5);
  
  // 标题
  noStroke();
  fill(50);
  textSize(12);
  textAlign(LEFT);
  text("v-t 图像", 10, 20);
  
  // 坐标系
  let ox = 50;
  let oy = h / 2;
  let graphW = w - 80;
  let graphH = (h - 40) / 2;
  
  stroke(150);
  strokeWeight(1);
  // x轴（时间轴）
  line(ox, oy, ox + graphW, oy);
  // y轴（速度轴）
  line(ox, 25, ox, h - 15);
  
  // 轴标签
  noStroke();
  fill(100);
  textSize(10);
  textAlign(CENTER);
  text("t", ox + graphW + 15, oy + 4);
  textAlign(RIGHT);
  text("0", ox - 5, oy + 4);
  text("v", ox - 5, 30);
  text("+", ox - 15, 35);
  text("-", ox - 15, h - 20);
  
  // 绘制斜率参考线（虚线）
  if (abs(a) > 0.05) {
    stroke(200, 100, 100, 100);
    strokeWeight(1);
    drawingContext.setLineDash([5, 5]);
    
    // 从当前点绘制斜率参考
    if (velocityData.length > 0) {
      let lastV = velocityData[velocityData.length - 1];
      let lastX = ox + (velocityData.length / maxDataPoints) * graphW;
      let lastY = oy - (lastV / 8) * graphH;
      
      // 绘制切线（斜率 = a）
      let dx = 30;
      let dy = -a * (dx / (graphW / maxDataPoints)) * (graphH / 8);
      line(lastX - dx, lastY + dy, lastX + dx, lastY - dy);
    }
    drawingContext.setLineDash([]);
  }
  
  // 绘制速度曲线
  if (velocityData.length > 1) {
    stroke(0, 150, 0);
    strokeWeight(2);
    noFill();
    beginShape();
    for (let i = 0; i < velocityData.length; i++) {
      let px = ox + (i / maxDataPoints) * graphW;
      let py = oy - (velocityData[i] / 8) * graphH;
      py = constrain(py, 25, h - 15);
      vertex(px, py);
    }
    endShape();
  }
  
  // 当前速度值
  noStroke();
  fill(0, 150, 0);
  textSize(11);
  textAlign(RIGHT);
  text("v = " + v.toFixed(1) + " m/s", w - 20, 20);
  
  // 斜率说明
  fill(200, 100, 100);
  textSize(10);
  text("斜率 = a = " + a.toFixed(1) + " m/s²", w - 20, 35);
}

// 绘制箭头
function drawArrow(x1, y1, x2, y2) {
  line(x1, y1, x2, y2);
  let angle = atan2(y2 - y1, x2 - x1);
  let arrowSize = 8;
  push();
  translate(x2, y2);
  rotate(angle);
  line(0, 0, -arrowSize, -arrowSize / 2);
  line(0, 0, -arrowSize, arrowSize / 2);
  pop();
}

// 更新物理状态
function updatePhysics() {
  // 更新速度
  v += a * (1 / 30);  // dt = 1/30 秒
  
  // 限制速度范围
  v = constrain(v, -6, 6);
  
  // 更新位置
  x += v * 2;  // 放大显示效果
  
  // 边界处理
  if (x > 650) {
    x = 650;
    v = 0;
  }
  if (x < 50) {
    x = 50;
    v = 0;
  }
  
  // 记录速度数据
  velocityData.push(v);
  
  // 限制数据长度
  if (velocityData.length > maxDataPoints) {
    velocityData.shift();
  }
  
  t++;
}

// 点击重置
function mousePressed() {
  // 检查是否点击在滑块区域外
  if (mouseY > 40 || mouseX > 170) {
    if (mouseX > 0 && mouseX < 700 && mouseY > 0 && mouseY < 420) {
      // 重置所有状态
      t = 0;
      x = 100;
      v = 0;
      velocityData = [];
      aSlider.value(0);
    }
  }
}
