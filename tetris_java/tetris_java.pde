import java.util.Random;

boolean left, right;
PVector position = new PVector(421, 35);

void setup(){
size(666, 700);
}

void createshape(float x, float y){
  Random rand = new Random();
  int shape = rand.nextInt(4) + 1;
  rect(x, y, 70, 70);
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
  createshape(position.x, position.y);
  position.y += 1;
}

void keyPressed(){
  if (keyCode == LEFT)
    position.x -= 35;
  else if (keyCode == RIGHT)
    position.x += 35;
}
