# Handbuch: Telegram-Bot mit ESP32 zur Aufnahme von Fotos und Türüberwachung
Es wurde sich an folgendem Tutorial orientiert: [telegram-control-esp32](https://randomnerdtutorials.com/telegram-control-esp32-esp8266-nodemcu-outputs/).
Der Code in Aufgabe 1 & 2 ist auch aus diesem übernommen.

In diesem Handbuch wird Schritt für Schritt erklärt, welche Vorbereitungen getroffen werden müssen um die Aufgaben des Arbeitsblattes [telegram-worksheet-student](/telegram/telegram-worksheet-student.md) durchführen zu können.

## Materialien
- ESP32 Mikrocontroller
- Kamera-Modul (z. B. OV2640 für ESP32-CAM)
- Mikro-USB-Kabel
- Arduino IDE
- Telegram-App

Für die vollständige Materialliste des Projektes siehe [materials](/setup/materials.md).

---

## Vorbereitungen
**Zunächst das Allgemeine Setup für den PC durchführen. Zu finden unter [start](/README.md) oder [pc-setup](/setup/pc-setup.md).**


### 1. Notwendige Bibliotheken installieren
1. Öffne die Arduino IDE.
2. Gehe zu `Werkzeuge > Bibliotheken verwalten`.
3. Suche und installiere die folgenden Bibliotheken:
   - `UniversalTelegramBot` by Brian Lough `Version 1.3.0`
   - `ArduinoJson` by Benoit Blanchon `Version 7.3.0`

---

### 2. Hardware vorbereiten
1. Verbinde den ESP32 mit deinem PC über das Mikro-USB-Kabel.
2. Falls du ein ESP32-CAM-Modul verwendest, schließe die Kamera nach Bedienungsanleitung korrekt an.

---

### 3. Code öffnen
1. Den Code für die die Aufgabe 1 & 2 des Arbeitsblattes findest du unter [telegram-led](/telegram/telegram-led/telegram-led.ino).
2. Den Code für Aufgabe 3 des Arbeitsblattes findest du unter [telegram-cam](/telegram/telegram-cam/).
3. Lade jeweils die benötigten Dateien herunter und öffne diese in der Arduino IDE.


### 4. Code Konfiguration
1. In beiden Code Dateien die Variablen `ssid` mit der SSID des zu verwendenden WLANS und `password` mit dem Passwort eintragen.
2. `Bottoken` und `ChatID` müssen hier noch **nicht** eingetragen werden, da diese auf den Arbeitsblättern neu generiert werden.
---

### 5. Hochladen und Testen des Codes (OPTIONAL)
Hierfür muss ein gültiger Telegram Bottoken und eine ChatID eingetragen werden. Siehe für eine Anleitung hierzu: [Aufgabe 1 Bot erstellen](/telegram/telegram-worksheet-teacher.md#aufgabe-1-bot-erstellen-api-schlüssel-und-chat-id-einrichten)
1. Finde den richtigen Port heraus.
   1. Suche im Geräte-Manager unter Anschlüsse (COM & LPT).
   2. finde heraus mit welchem Port der ESP32 verbunden ist.
2. Wähle in der Arduino IDE das richtige Board und den Port unter `Werkzeuge > Board > esp` und `Werkzeuge > Port`. (AI Thinker ESP32-CAM oder ESP32 Wrover Module)
3. Lade den Code auf den ESP32 hoch. (Pfeil oben links)
4. Öffne den Serial Monitor (Baudrate 115200), um sicherzustellen, dass alles funktioniert.
5. Teste die Funktionen des Bots
---
