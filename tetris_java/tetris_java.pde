import java.util.Random;

boolean left, right;
Random rand = new Random();
int shape = rand.nextInt(7) + 1;
PVector position = new PVector(421, 35);
int angle;

void setup(){
size(666, 700);
}

void randomnum(){    
  shape = rand.nextInt(7) + 1;
}
void createshape(int shape, float x, float y){
  strokeWeight(3);
  strokeCap(PROJECT);
  stroke(0, 0, 0);
  switch(shape) {
    case 1:
      // 'I' block
      stroke(0, 0, 0);
      fill(0, 255, 255);
      rect(x,y, 35, 140);
      line(x, y + 35 , x + 35, y + 35);
      line(x, y + 70, x + 35, y + 70);
      line(x, y + 105, x + 35, y + 105);
      break;
    case 2: 
      // Square block
      fill(255, 255, 0);
      rect(x, y, 70, 70);
      line(x + 35, y, x + 35, y + 70);
      line(x, y + 35, x + 70, y + 35);
      break;
    case 3:
      // 'T' block
      fill(255, 0, 255);
      beginShape();
      vertex(x, y);
      vertex(x, y + 35);
      vertex(x - 35, y + 35);
      vertex(x - 35, y + 70);
      vertex(x + 70, y + 70);
      vertex(x + 70, y + 35);
      vertex(x + 35, y + 35);
      vertex(x + 35, y);
      endShape(CLOSE);
      line(x, y + 35, x + 35, y + 35);
      line(x, y + 35, x, y + 70);
      line(x + 35, y + 35, x + 35, y + 70);
      break;
    case 4:
      // 'L' block
      fill(255, 165, 0); 
      beginShape();
      vertex(x + 70, y);
      vertex(x + 70, y + 35);
      vertex(x, y + 35);
      vertex(x, y + 70);
      vertex(x + 105, y + 70);
      vertex(x + 105, y);
      endShape(CLOSE);
      line(x + 35, y + 35, x  + 35, y + 70);
      line(x + 70, y + 35, x + 70, y + 70);
      line(x + 70, y + 35, x + 105, y + 35);
      break;
    case 5:
      // 'J' block
      fill(0, 0, 255);
      beginShape();
      vertex(x, y);
      vertex(x, y + 70);
      vertex(x + 105, y + 70);
      vertex(x + 105, y + 35);
      vertex(x + 35, y + 35);
      vertex(x + 35, y);
      endShape(CLOSE);
      line(x, y + 35, x + 35, y + 35);  
      line(x + 35, y + 35, x + 35, y + 70);
      line(x + 70, y + 35, x + 70, y + 70);
      break;
    case 6:
      // 'S' block
      fill(0, 255, 0);
      beginShape();
      vertex(x, y);
      vertex(x, y + 35);
      vertex(x - 35, y + 35);
      vertex(x - 35, y + 70);
      vertex(x + 35, y + 70);
      vertex(x + 35, y + 35);
      vertex(x + 70, y + 35);
      vertex(x + 70, y);
      endShape(CLOSE);
      line(x, y + 35, x + 35, y + 35);
      line(x, y + 35, x, y + 70);
      line(x + 35, y, x + 35, y + 35);
      break;
    case 7:
      // 'Z' block
      fill(255, 0, 0);
      beginShape();
      vertex(x, y);
      vertex(x, y + 35);
      vertex(x + 35, y + 35);
      vertex(x + 35, y + 70);
      vertex(x + 105, y + 70);
      vertex(x + 105, y + 35);
      vertex(x + 70, y + 35);
      vertex(x + 70, y);
      endShape(CLOSE);
      line(x + 35, y, x + 35, y + 35);
      line(x + 35, y + 35, x + 70, y + 35);
      line(x + 70, y + 35, x + 70, y + 70);
      break;
  } 
}

void draw(){
  background(0);
  stroke(128);
  strokeWeight(1);
  line(316, 0, 316, height);
  for (int i = 316; i <= width; i += 35)
    line(i, 0, i, height);
  for (int i = 0; i <= height; i += 35)
    line(316, i,  width, i);
  
  switch(shape) {
    case 1:
      switch(angle % 360) {
        case 0:
          position.x = constrain(position.x, 316, width - 35); break;
        case 90:
          position.x = constrain(position.x, 386,  width - 70); break;
        case 180:
          position.x = constrain(position.x, 281, width - 70); break;
        case 270:
          position.x = constrain(position.x, 316, width - 140); break;
        default: break;
      }
      break;
    case 2:
      position.x = constrain(position.x, 316, width - 70); break;
    case 3:
      switch(angle % 360) {
        case 0: position.x = constrain(position.x, 351, width - 70); break;
        case 90: position.x = constrain(position.x, 316, width - 70); break;
        case 180: position.x = constrain(position.x, 316, width - 105); break;
        case 270: position.x = constrain(position.x, 316, width - 70); break;
      }
      break;
    case 4: case 5:
      switch(angle % 360) {
      case 0: position.x = constrain(position.x, 316, width - 105); break;
      case 90: position.x = constrain(position.x, 316, width - 70); break;
      case 180: position.x = constrain(position.x, 351, width - 70); break;
      case 270: position.x = constrain(position.x, 316, width - 70); break;
      }
      break;
    case 6:
    switch(angle % 360) {
      case 0: position.x = constrain(position.x, 351, width - 70); break;
      case 90: case 270: position.x = constrain(position.x, 316, width - 70); break;
      case 180: position.x = constrain(position.x, 316, width - 105); break;
    }
    break;
    case 7:
      switch(angle % 360) {
      case 0: position.x = constrain(position.x, 316, width - 105); break;
      case 90: case 270: position.x = constrain(position.x, 316, width - 70); break;
      case 180: position.x = constrain(position.x, 351, width - 70); break;
      }
      break;
  }
  pushMatrix();
  translate(position.x + 35, position.y + 35);
  rotate(radians(angle));
  createshape(shape, -35, -35);
  popMatrix();
  
  if (position.y > height - 70) {
    position.set(421.0, 35.0);
    randomnum();
    angle = 0;
    
  } 
    
  position.y += 1;
}

void keyPressed(){
  if (keyCode == LEFT)
    position.x -= 35;
  else if (keyCode == RIGHT)
    position.x += 35;
  else if (keyCode == UP)
    angle += 90;
  else if (keyCode == DOWN)
    angle += 270;
  else if (key == ' ')
    position.y += 35;
}
