let t = 0;
let dt = 0.02;
const T_MAX = 10;

let displacement = [];
let distance = [];

let lastX = 0;
let totalDistance = 0;

function setup() {
  createCanvas(900, 420);
  lastX = motion(0);
}

function draw() {
  background(255);
  drawLeftMotion();
  drawGraphs();
  updateData();
}

function motion(time) {
  return 100 * sin((TWO_PI / T_MAX) * time);
}

function updateData() {
  let x = motion(t);
  let s = x;
  let dx = abs(x - lastX);
  totalDistance += dx;

  displacement.push(s);
  distance.push(totalDistance);

  lastX = x;
  t += dt;

  if (t > T_MAX) {
    t = 0;
    displacement = [];
    distance = [];
    totalDistance = 0;
    lastX = motion(0);
  }
}

/* -------- 左侧：直线运动 + 位移 -------- */
function drawLeftMotion() {
  push();
  translate(120, height / 2);

  // x轴
  stroke(0);
  line(-150, 0, 150, 0);

  // 刻度
  for (let i = -100; i <= 100; i += 50) {
    line(i, -5, i, 5);
    noStroke();
    fill(0);
    textAlign(CENTER);
    text(i, i, 20);
    stroke(0);
  }

  // 原点
  fill(0);
  text("O", 0, -10);

  // 小球
  let x = motion(t);
  fill(50);
  ellipse(x, 0, 20, 20);

  // 位移向量
  stroke(0);
  line(0, -25, x, -25);
  fill(0);
  triangle(x, -25, x - 6, -20, x - 6, -30);
  noStroke();
  text("s", x / 2, -30);

  pop();
}

/* -------- 右侧：图像 -------- */
function drawGraphs() {
  drawGraph(
    displacement,
    360,
    40,
    -120,
    120,
    "位移 - 时间图  s-t"
  );

  drawGraph(
    distance,
    360,
    230,
    0,
    300,
    "路程 - 时间图  l-t"
  );
}

function drawGraph(data, ox, oy, ymin, ymax, label) {
  push();
  translate(ox, oy);

  stroke(0);
  noFill();
  rect(0, 0, 260, 140);

  // 坐标轴刻度
  for (let i = 0; i <= 10; i += 5) {
    let x = map(i, 0, T_MAX, 0, 260);
    line(x, 140, x, 145);
    noStroke();
    fill(0);
    text(i + "s", x, 160);
    stroke(0);
  }

  for (let y = ymin; y <= ymax; y += (ymax - ymin) / 4) {
    let py = map(y, ymin, ymax, 120, 20);
    line(-5, py, 0, py);
    noStroke();
    fill(0);
    text(y, -25, py + 4);
    stroke(0);
  }

  // 曲线
  beginShape();
  for (let i = 0; i < data.length; i++) {
    let x = map(i * dt, 0, T_MAX, 0, 260);
    let y = map(data[i], ymin, ymax, 120, 20);
    vertex(x, y);
  }
  endShape();

  noStroke();
  fill(0);
  text(label, 0, -10);
  pop();
}
