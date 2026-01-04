int buttons[6];

int buttons[0] = 2;

int notes[] = {262, 294, 330, 349};

void setup() {
    Serial.begin(9600);

}

void loop() {
    int keyValue = analogRead(A0);
    Serial.println(keyValue);
    if (keyValue == 1023) {
        tone(2, notes[0]);
    }
    else if (keyValue >= 990 && keyValue <= 1010) {
        tone(2, notes[1]);
    }
    else if (keyValue >= 505 && keyValue <= 515) {
        tone(2, notes[2]);
    }
    else if (keyValue >= 5 && keyValue <= 10) {
        tone(2, notes[3]);
    }
    else {
        noTone(8);
    }
}
