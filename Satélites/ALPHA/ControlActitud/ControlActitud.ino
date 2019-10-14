<<<<<<< HEAD
<<<<<<< HEAD

void setup() {
 
=======
#include <Servo.h>

Servo esc;
void setup() {
  esc.attach(11);
  esc.writeMicroseconds(1000);
  Serial.begin(9600);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
}
void loop() {
  
  int val=analogRead(A0);
  val=map(val,0,1023,1250,1750);
  Serial.println(val);
  esc.writeMicroseconds(val);
>>>>>>> ESC
=======
#include <Wire.h>
#include <SparkFunLSM9DS1.h>

LSM9DS1 imu;

#define LSM9DS1_M  0x1E // Would be 0x1C if SDO_M is LOW
#define LSM9DS1_AG  0x6B // Would be 0x6A if SDO_AG is LOW

#define PRINT_SPEED 250 // 250 ms between prints
static unsigned long lastPrint = 0; // Keep track of print time
#define DECLINATION -8.58 // Declination (degrees) in Boulder, CO.

void setup() {
  Serial.begin(9600);
  imu.settings.device.commInterface = IMU_MODE_I2C;
  imu.settings.device.mAddress = LSM9DS1_M;
  imu.settings.device.agAddress = LSM9DS1_AG;

  if (!imu.begin())
  {
    Serial.println("Failed to communicate with LSM9DS1.");
    for(;;);
  }
}

void loop() {
  Attitude result=imu.getAttitude();
  Serial.print(result.roll, 2);
  Serial.print("\t");
  Serial.print(result.pitch, 2);
  Serial.print("\t");
  Serial.println(result.yaw, 2);
      
>>>>>>> IMU
}
