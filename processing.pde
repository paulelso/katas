// Recommended code 
int puntos = 3;
int player = 487;
int bolaX = 300;
int bolaY = 300;
int velocidadX = 5;
int velocidadY = 5;
color colorNumero = color(#00FF00);

void setup() {
  size(1200, 600);
}

void jugar() {
  fill(colorNumero);
  textSize(100);
  text(puntos, 25, 100);
  strokeWeight(8);
  stroke(#000000);
  fill(#A000FF);
  rect(player, 525, 225, 50);
  ellipse(bolaX, bolaY, 50, 50);
  bolaX += velocidadX;
  bolaY += velocidadY;
  
  if (bolaX < 26 || bolaX > 1174) {
    velocidadX = -velocidadX;
  }
  
  if (bolaY < 26) {
    velocidadY = -velocidadY;
  }
  
  if (bolaY > 574) {
    puntos--;
    velocidadY = -velocidadY;
  }
  
  if (bolaY > 525 && bolaY < 575 && bolaX > player && bolaX < player + 225) {
    velocidadY = -velocidadY;
  }
}

void draw() {
  background(#00FFFF);
  
  if (puntos == 0) {
    fill(#FF0000);
    textSize(100);
    text("Game over", 335, 200);
    noLoop(); // End the game
  } else if (puntos == 3) {
    colorNumero = color(#00FF00);    
  } else if (puntos == 2) {
    colorNumero = color(#FFFF00);
  } else if (puntos == 1) {
    colorNumero = color(#FF0000);
  }
  
  jugar();
}