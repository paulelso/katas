// Initialize variables
int puntos = 3;
int player = 487;
int bolaX = 300;
int bolaY = 300;
int velocidadX = 5;
int velocidadY = 5;
color colorNumero = color(#00FF00);
int cajaRoja = 300;
int cajaVerdeX = 925;
int cajaRojaY = 0;
int cajaVerdeY = 130;
void setup() {
  size(1200, 600);
}
void draw() {
  background(#00FFFF);
  // Check if the game is over
  if(puntos == 0) {
    fill(#FF0000);
    textSize(100);
    text("Game over", 350, 200);
    noLoop();
  } else {
    // Display points with different colors based on the number of points
    if(puntos == 3) {
      colorNumero = color(#00FF00);    
    } else if(puntos == 2) {
      colorNumero = color(#FFFF00);
    } else if(puntos == 1) {
      colorNumero = color(#FF0000);
    }
    jugar(); // Call the game function
  }
}
void jugar() {
  fill(colorNumero);
  textSize(100);
  text(puntos, 25, 100);
  strokeWeight(8);
  stroke(#000000);
  ellipse(bolaX, bolaY, 50, 50);
  fill(#A000FF);
  rect(player, 525, 225, 50);
  fill(#FF0000);
  rect(cajaRoja, 180, 75, 75);
  fill(#00FF00);
  rect(cajaVerdeX, cajaVerdeY, 75, 75);
  bolaX = bolaX + velocidadX;
  bolaY = bolaY + velocidadY;
  //cajaRoja subtracts 1 point per hit with ball
  if (bolaY > 180 && bolaY < 225) {
    if (bolaX > cajaRoja && bolaX < cajaRoja + 75) {
      velocidadX = -velocidadX;
      velocidadY = -velocidadY;
      puntos--; // Subtract one point per hit
    }
    else if (bolaX > cajaVerdeX && bolaX < cajaVerdeX + 75) {
      velocidadX = -velocidadX;
      puntos++; // Add one point per hit
    }
  }
  //cajaVerde adds 1 point per hit with ball
  if (bolaY > cajaVerdeY && bolaY < cajaVerdeY + 75) {
    if (bolaX > cajaVerdeX && bolaX < cajaVerdeX + 75) {
      puntos++; // Subtract one point per hit
        if(bolaX > cajaVerdeX && bolaX < cajaVerdeX + 75) {
          velocidadX = -velocidadX;
        }
        else {
          if(bolaY > cajaVerdeY && bolaY < cajaVerdeY + 75) {
            velocidadY = -velocidadY;
          }
          else {
            if(bolaX > cajaVerdeY && bolaX < cajaVerdeY + 75) {
              velocidadX = -velocidadX;
            }
            else {
              if(bolaY > cajaVerdeX && bolaY < cajaVerdeX + 75) {
                velocidadY = -velocidadY;
              }
            }
          }
        }      
      }
    }
  // Collision detection with walls
  if(bolaX < 26 || bolaX > 1174) {
    velocidadX = -velocidadX;
  }
  if(bolaY < 26) {
    velocidadY = -velocidadY;
  }
  if(bolaY > 574) {
    velocidadY = -velocidadY;
    puntos = puntos -1;
  }
  // Collision detection with paddle
  if(bolaY > 525 && bolaY < 575) {
    if(bolaX > player && bolaX < player + 225) {
      velocidadY = -velocidadY;
    }
  }
}
void keyPressed() {
  // Move the paddle left or right using 'a' and 'd' keys
  if(key == 'a') {
    player = max(player - 30, 0); // Ensure the paddle does not go out of bounds
  }
  if(key == 'd') {
    player = min(player + 30, width - 225); // Ensure the paddle does not go out of bounds
  }
}
