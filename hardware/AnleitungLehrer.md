# ESP32 Türsensor Projekt

## Ziel der Stunde:
In diesem Projekt lernen die Schüler, wie sie den ESP32 verwenden, um einen Türsensor anzuschließen und den Status der Tür zu visualisieren. Der Status (offen oder geschlossen) wird durch eine LED angezeigt.

## Ablauf

### 1. Einführung (5 Minuten)
- **Zielvorstellung:**
    - Es wird gezeigt wie man mit ESP32 umgeht, um mit einem Türsensor zu arbeiten.
  
- **Vorstellung der Komponenten:**
  - **ESP32 Wrover Kit:** GPIO-Pins, Stromversorgung, serielle Schnittstelle.
  - **Türsensor:** Wie er erkennt, ob eine Tür geöffnet oder geschlossen ist.
  - **LED:** Visualisierung des Zustands.
  
  **Hinweis zur LED:**  
  Bei einer LED gibt es zwei Elektroden:  
  - **Anode (positive Elektrode):** Längeres Bein, verbunden mit dem positiven Pol (z. B. GPIO-Pin des ESP32).
  - **Kathode (negative Elektrode):** Kürzeres Bein, verbunden mit dem negativen Pol (GND).  
  Die Anode und Kathode sorgen dafür, dass der Strom nur in eine Richtung fließen kann und die LED leuchtet.

---

### 2. Hardware-Aufbau (15 Minuten)

#### Schritt-für-Schritt-Anleitung

**ESP32 vorbereiten:**
- Schließe den ESP32 an das Steckbrett an und überprüfe, wie die Pins nummeriert sind.

**Türsensor anschließen:**
- Verbinde den Türsensor mit dem ESP32:
  - Signal-Pin → GPIO 12
  - GND → GND (vom ESP32)
  - **Hinweis:** Falls kein interner Pull-up-Widerstand verwendet wird, füge einen externen Widerstand hinzu.

**LED anschließen:**
- Anode (langer Pin) → GPIO 25.
- Kathode (kurzer Pin) → GND.

**Schaltkreis prüfen:**
- Kontrolliere alle Verbindungen, um sicherzustellen, dass alles richtig angeschlossen ist.

---

### 3. Programmierung (20 Minuten)

#### Schritt-für-Schritt-Anleitung

**Arduino IDE einrichten:**
- Wähle das ESP32-Board aus und stelle die serielle Schnittstelle korrekt ein.

**Code durchgehen:**
- **`pinMode()`**: Erkläre, warum dies wichtig ist, um Pins als Eingänge oder Ausgänge zu definieren.
- **`digitalRead()`**: Zeige, wie der Zustand des Türsensors gelesen wird.
- **`if (currentSensorState != previousSensorState)`**: Erkläre, warum nach Änderungen im Sensorstatus gesucht wird.

**Code hochladen:**
- Lade den Code auf das ESP32 und öffne den seriellen Monitor.
- Beobachte gemeinsam mit den Schülern, wie der Monitor sich verändert, wenn der Sensor betätigt wird.

**Test durchführen:**
- Zeige, wie sich der LED-Zustand ändert, wenn die Tür geöffnet oder geschlossen wird.
- Lass die Schüler den Sensor testen und die Ergebnisse beobachten.

---

### 4. Abschluss (5 Minuten)

#### Zusammenfassung:
- Was haben die Schüler gelernt?
  - Wie funktioniert der Türsensor?
  - Wie kann man den Zustand der Tür mit einer LED visualisieren?
  - Welche Schritte waren notwendig, um das Projekt umzusetzen?

- Beantworte Fragen und biete Unterstützung an, falls es Unklarheiten gibt.

---

## Hinweise:
- Achte darauf, dass die Schüler alle Schritte genau folgen und sicherstellen, dass ihre Verbindungen korrekt sind.
- Wenn Schüler Schwierigkeiten haben, biete individuelle Hilfe bei der Verkabelung und Programmierung an.
- Das Übungsblatt ist optional.
