#include <Stepper.h>
#include <Servo.h>

const int stepsPerRevolution = 2048;
Stepper myStepper(stepsPerRevolution, 9, 11, 10, 12);
Servo myServo;

int servoPos = 90;


void setup() {
 Serial.begin(9600);
 myStepper.setSpeed(12);
 myServo.attach(13);
 myServo.write(servoPos);
}
void loop() {
 if (Serial.available() > 0) {
    char command = Serial.read();
 if (command == 'U') {
    if (servoPos > 10) servoPos -= 1; 
        myServo.write(servoPos);
 }
 else if (command == 'D') {
    if (servoPos < 170) servoPos += 1;
       myServo.write(servoPos);
 }
 
 if (command == 'L') {
    myStepper.step(10); 
 }
 else if (command == 'R') {
    myStepper.step(-10);
 }
 }
}