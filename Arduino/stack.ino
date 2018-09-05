#include <Servo.h>

// For Arduino Uno
// Perfect plays Stack with servo

int upPosition   =  110;
int downPosition = 135;
int baseInsertPos = 40;
int pinServo = 9;

Servo my_servo;


void setup() {
  my_servo.attach(pinServo);
  my_servo.write(80);
  
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  delay(3000);
  digitalWrite(13, LOW);
  
  my_servo.write(downPosition);
  delay(200);
  my_servo.write(upPosition);
  delay(770);
}

void loop() {
  my_servo.write(downPosition); //1
  delay(200);
  my_servo.write(upPosition);//0
  delay(600);
}