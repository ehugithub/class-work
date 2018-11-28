import java.util.Random;
void setup(){
size(666, 700);


boolean left, right;
PVector position;
position = new PVector(421, 35);
}
void createshape(int x, int y){
  Random rand = new Random();
  int shape = rand.nextInt(4) + 1;
  rect(x, y, 70, 70);
}

void draw(){
  background(0);
  stroke(128);
  createshape(0,0);
  line(316, 0, 316, height);
  for (int i = 316; i <= height; i += 35)
    line(i, 0, i, height);
}

void keyPressed(){
  
}
