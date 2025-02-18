## 1. Einführung

Heute zeigen wir euch, wie ein ESP32 genutzt wird, um mit einem Türsensor zu arbeiten. Ihr werdet den Status ‘Tür offen‘ oder ‘Tür geschlossen‘ visualisieren und verstehen, wie das funktioniert.

### Vorstellung der Komponenten:
- **ESP32 Wrover Kit:** GPIO-Pins, Stromversorgung, serielle Schnittstelle.
- **Türsensor:** Wie er erkennt, ob eine Tür geöffnet/geschlossen ist.
- **LED:** Visualisierung des Zustands.
### Bemerkung:
Bei einer LED gibt es zwei Elektroden: <br/>
**Anode (positive Elektrode):** Dies ist das längere Bein der LED und muss mit dem positiven Pol (z. B. GPIO-Pin des ESP32) verbunden werden.
**Kathode (negative Elektrode):** Dies ist das kürzere Bein der LED und wird mit dem negativen Pol (z. B. GND) verbunden.  <br/>
Die Anode und Kathode sorgen dafür, dass der Strom nur in eine Richtung durch die LED fließen kann, wodurch sie leuchtet. <br/>

<img src="https://github.com/user-attachments/assets/9c0e4d38-b900-4361-8f6c-774c9f128e54" alt="" width="100"/>

## 2. Hardware-Aufbau

### Schritt-für-Schritt-Anleitung:

#### ESP32 vorbereiten:
- Schließe den ESP32 an das Steckbrett an.
- Achte wie die Pins auf dem Board nummeriert sind.

#### Sensor anschließen:
- Verbinde den Türsensor:
  - Signal-Pin → GPIO 12.
  - GND → GND (vom ESP32).
- **Hinweis:** Falls kein interner Pull-up-Widerstand verwendet wird, einen externen Widerstand hinzufügen.

#### LED anschließen:
- Anode (langer Pin) → GPIO 25.
- Kathode (kurzer Pin) → GND.

#### Schaltkreis prüfen:
- Kontrolliere alle Verbindungen.
<img src="https://github.com/user-attachments/assets/63dd42df-e0a4-47e1-af5f-915875424428" alt="" width="300"/>

## 3. Programmierung 

### Schritt-für-Schritt-Anleitung:

#### Arduino IDE einrichten:
- Wähle das ESP32-Board aus.
- Stelle die richtige serielle Schnittstelle ein.

#### Code durchgehen:
- Gebe den vorbereiteten Code Zeile für Zeile ein und erkläre:
  - Was macht `pinMode()`?
  - Wie funktioniert `digitalRead()`?
  - Warum nutzen wir `if (currentSensorState != previousSensorState)`?

#### Code hochladen:
- Lade den Code hoch und öffne den seriellen Monitor, damit was auf dem Bildschirm angezeigt wird.

#### Test durchführen:
- Zeige, wie der Sensor auf Zustandsänderungen (Tür geöffnet/geschlossen) reagiert.
- Beobachte die LED.
