# esp32-doorbot
# Installationsanleitung und Systemanforderungen

## 1. Einleitung

### Projektname
**Arduino für ESP32-Integration auf einem Laptop konfigurieren**

### Projektbeschreibung
Dieses Projekt beschreibt die Systemanforderungen und Konfigurationsschritte, die notwendig sind, um eine einfache und zuverlässige Kommunikation zwischen einem Laptop und einem angeschlossenen ESP32-Modul herzustellen. Es umfasst Funktionen zur Steuerung, Konfiguration und Datenübertragung.

### Zielgruppe
- Schüler
- Dozenten
- Studenten

### Ziele des Projekts
- Bereitstellung einer stabilen Verbindung zwischen Laptop und ESP32-Modul.
- Definition der Systemanforderungen für ESP32-Module.
- Bereitstellung einer Schritt-für-Schritt-Anleitung zur Installation und Konfiguration der Arduino-Umgebung für ausgewählte Projekte.

---

## 2. Anforderungen

### 2.1 Systemanforderungen
- **Betriebssystem**: Windows 10 oder neuer
- **Software**: 
  - Arduino IDE 2.0 oder neuer
  - Telegram 5.9.0 oder neuer

### 2.2 Hardwareanforderungen
- **Option 1**: ESP32 Wrover Kit & USB-C Kabel
- **Option 2**: ESP32-CAM & Micro-USB Kabel

---

## 3. Installationsanleitung

### 3.1 Einrichtung der Arduino IDE für ESP32 (Wrover Kit & ESP32-CAM)

#### Schritt 1: Arduino IDE starten
- Öffnen Sie die Arduino IDE auf Ihrem System.

#### Schritt 2: Zusätzliche Boardverwalter-URLs konfigurieren
1. Navigieren Sie in der Arduino IDE zu **Datei > Einstellungen**.
2. Geben Sie unter **Zusätzliche Boardverwalter-URLs** die folgende URL ein:  
   `https://dl.espressif.com/dl/package_esp32_index.json`
3. Bestätigen Sie mit **OK**.

#### Schritt 3: ESP32 Boards installieren
1. Öffnen Sie den **Boardverwalter** über **Werkzeuge > Board > Board-Verwaltung**.
2. Suchen Sie nach **esp32** und installieren Sie das Paket **esp32 von Espressif Systems**.
3. Im Falle der Verwendung des **CamServers** muss außerdem noch das Paket **Arduino Json** installiert werden.

#### Schritt 4: ESP32-Board auswählen
- Für **DoorBot**: Navigieren Sie zu **Werkzeuge > Board > esp32** und wählen Sie **ESP32 Wrover Kit (alle)** aus.
- Für **ChatBot**: Navigieren Sie zu **Werkzeuge > Board > esp32** und wählen Sie **ESP32 Dev Module** aus.
- Für **CamServer**: Navigieren Sie zu **Werkzeuge > Board > esp32** und wählen Sie **AI Thinker ESP32-CAM**.

#### Schritt 5: Upload-Geschwindigkeit anpassen
- Stellen Sie unter **Werkzeuge > Upload Speed** die Geschwindigkeit auf **115200** ein.

#### Schritt 6: Port des ESP32-Moduls auswählen
1. Öffnen Sie den **Geräte-Manager** auf Ihrem System.
2. Suchen Sie unter **Ports (COM & LPT)** den Port, der Ihrem ESP32-Modul zugeordnet ist.
3. Wählen Sie diesen Port über die **Ribbon-Bar** in der Arduino IDE aus.

#### Schritt 7: Code hocHladen
- Laden Sie die entsprechende **.ino**-Datei, die Sie für Ihr Projekt verwenden möchten, in die Arduino IDE hoch.

#### Schritt 8: WLAN und Bot-Konfiguration
1. Tragen Sie die folgenden Informationen ein, um die Verbindung zum ESP32-Modul zu gewährleisten:
   - WLAN-SSID      (Name des Netzwerks)
   - WLAN-Passwort  (Passwort des Netzwerks)
   - Bot-Token      (Token, welches auf den entsprechenden Telegram-Bot verweist - Erstellung des Tokens mittels BotFather)
   - ChatID         (ID des entsprechenden Chats des Bots)

**_Dieser Schritt kann bei der Verwendung des DoorBots ausgelassen werden._**

#### Schritt 9: Kompilieren und Hochladen des Codes
1. Kompilieren Sie den Code über die **Ribbon-Bar** in der Arduino IDE.
2. Laden Sie den kompilierten Code auf das ESP32-Modul hoch.

---

### 3.2 Verwendung des Cam-Servers
1. Öffnen Sie innerhalb der Arduino IDE das Beispiel des CamerWebServers über **Datei > Beispiele > ESP32 > Camera > CameraWebServer**.
2. Nehmen Sie folgende Einstellungen vor:
   - Fügen Sie die Zeile `#define AI_THINKER_CAMERA_MODEL` - sofern Sie dieses Model verwenden - zum Code hinzu.
   - Wählen Sie im Board Manager den **AI Thinker ESP32-CAM** aus.
   - Auch hier müssen Sie die SSID und das Passworts des Netzwerks eintragen.
   - Stellen Sie die Baudrate auf **115200** ein.
3. Schließen Sie den ESP32 an den Computer an und laden Sie den Code hoch.
4. Öffnen Sie den **Serial Monitor** über **Werkzeuge > Serial Monitor** in der Arduino IDE.
5. Drücken Sie anschließend den Reset-Knopf auf dem ESP32 und notieren Sie sich die angezeigte IP-Adresse.
6. Öffnen Sie die Datei `camera_pins.h` innerhalb des Beispielprojekts, um die Pin-Konfiguration für die verschiedenen ESP32-Modelle, die der Code verwendet, zu verstehen.
7. Kopieren Sie die im Serial Monitor angezeigte IP-Adresse und fügen Sie sie in einem Browser ein, um im Web-Interface die Kamera zu testen.

---

Diese Anleitung dient als Grundlage für die Konfiguration und Nutzung Ihrer ESP32-Hardware. Weitere Details und spezifische Beispiele finden Sie in den entsprechenden Dokumentationsabschnitten oder Tutorials.

