int sensorValue;
int sensorLow = 1023;
int sensorHigh = 0;

const int ledPin = 2;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);

  while (millis() < 5000) {
    // Wait for 5 seconds to allow sensor stabilization
    sensorValue = analogRead(A1);
    if (sensorValue < sensorLow) {
      sensorLow = sensorValue;
    }
    if (sensorValue > sensorHigh) {
      sensorHigh = sensorValue;
  
    } 
    }
    digitalWrite(ledPin, LOW);

}
void loop() {
  sensorValue = analogRead(A1);

  int pitch = map(sensorValue, sensorLow, sensorHigh, 50, 4000);
  tone(2, pitch, 20);

  delay(10);
}
