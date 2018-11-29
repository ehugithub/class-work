import java.util.Random;

boolean left, right;
PVector position = new PVector(421, 35);
int angle;

void setup(){
size(666, 700);
}

void createshape(float x, float y){
  Random rand = new Random();
  int shape = rand.nextInt(7) + 1;
  switch(shape) {
    case 1: rect(x,y, 35, 140); // 'I' block
    case 2: rect(x, y, 70, 70); // Square block
    case 3: // 'T' block
    case 4: // 'J' block
    case 5: // 'L' block
    case 6: // 'S' block
    case 7: // 'Z' block
  }
  //rect(x,y, 35, 140);
  //rect(x, y, 70, 70);
}

void draw(){
  background(0);
  stroke(128);
  line(316, 0, 316, height);
  for (int i = 316; i <= width; i += 35)
    line(i, 0, i, height);
  for (int i = 0; i <= height; i += 35)
    line(316, i,  width, i);
    
  
  position.x = constrain(position.x, 316, width - 70);
  pushMatrix();
  translate(position.x + 35, position.y + 35);
  rotate(radians(angle));
  createshape(-35, -35);
  popMatrix();
  
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
    angle -= 90;
}
