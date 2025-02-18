#define SENSOR_PIN 12 // GPIO-Pin, mit dem das Signal-Kabel verbunden ist

// Variablen für den vorherigen Zustand des Sensors
int previousSensorState = HIGH;

void setup() {
  // Serieller Monitor zur Fehlersuche
  Serial.begin(115200);

  // Sensor-Pin als Eingang mit Pull-up-Widerstand definieren
  pinMode(SENSOR_PIN, INPUT_PULLUP);
  pinMode(25, OUTPUT); // LED oder anderes Ausgabegerät

  Serial.println("Türsensor-Setup abgeschlossen!");
}

void loop() {
  // Zustand des Sensors lesen
  int currentSensorState = digitalRead(SENSOR_PIN);

  // Nur bei Zustandsänderung ausgeben
  if (currentSensorState != previousSensorState) {
    // Zustand hat sich geändert, aktualisieren und ausgeben
    if (currentSensorState == LOW) {
      Serial.println("Tür geschlossen."); // Sensor erkannt, Tür ist zu
      digitalWrite(25, HIGH);             // LED an (Tür geschlossen)
    } else if (currentSensorState == HIGH) {
      Serial.println("Tür geöffnet!");    // Sensor nicht erkannt, Tür ist offen
      digitalWrite(25, LOW);              // LED aus (Tür geöffnet)
    }

    // Vorherigen Zustand aktualisieren
    previousSensorState = currentSensorState;
  }

  delay(50); // Kurze Verzögerung zur Entprellung des Sensors
}
