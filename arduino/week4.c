const int ledPin = 13;
int bval = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  
  int serialValue = Serial.read();
  if (serialValue != -1) bval = serialValue;
  if (bval == 49) digitalWrite(ledPin, HIGH);//First value read of the ascii for 1
  if (bval == 48) digitalWrite(ledPin, LOW);//First value read of the ascii for 0
//   To debug:
//   Serial.print(serialValue);
//   Serial.print("\t");
//   Serial.println(bval); 
}