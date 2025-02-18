
# ESP32 Face Recognition

Dieses Projekt zeigt, wie ein ESP32-CAM-Modul mit einer Kamera und einem Python-Skript verwendet werden kann, um Gesichtserkennung durchzuführen. 

## Materialien

- ESP32-CAM Modul (z. B. mit OV2640 Kamera)
- Mikro-USB-Kabel
- Arduino IDE
- Python mit OpenCV
- Haarcascade-Datei für die Gesichtserkennung

---

## Vorbereitung

### 1. Python-Umgebung einrichten
1. Installiere [Python](https://python.org).
2. Stelle sicher, dass `pip` installiert ist:
   ```bash
   pip --version
   ```
3. Installiere die notwendigen Bibliotheken:
   ```bash
   pip install opencv-python numpy
   ```

### 2. ESP32 einrichten
1. Lade die [Arduino IDE](https://www.arduino.cc/en/software) herunter.
2. Öffne das Beispiel `CameraWebServer` in der Arduino IDE:
   - Datei → Beispiele → ESP32 → Camera → CameraWebServer.
<img width="976" alt="image" src="https://github.com/user-attachments/assets/c518501b-dfce-4b8f-80af-b9f57d8d1d2a" />

3. Passe folgende Einstellungen im Code an:
   - Wähle das richtige Board (z. B. `AI Thinker ESP32-CAM`).
<img width="894" alt="image" src="https://github.com/user-attachments/assets/a24b2084-2b8b-4ebe-b70c-f362e22e5b7b" />

   - Setze SSID und Passwort:
     ```cpp
     const char* ssid = "DEIN_NETZWERK";
     const char* password = "DEIN_PASSWORT";
     ```
4. Lade den Code auf das ESP32-CAM-Modul hoch.
5. Öffne den Serial Monitor und notiere dir die IP-Adresse des ESP32-CAM.
   - Reset-Button auf ESP32-Board drücken, falls Serial Monitor noch nicht geöffnet war
   - Baud Rate im Serial Monitor auf (115200) ändern

---

## Gesichtserkennung mit Python

### 1. Haarcascade-Datei hinzufügen
- Stelle sicher, dass die Haarcascade-Datei für die Gesichtserkennung verfügbar ist:
  `haarcascade_frontalface_default.xml`. Sie ist in OpenCV enthalten und befindet sich normalerweise unter:
  ```
  C:\Users\"USER"\AppData\Local\Programs\Python\"PYTHON+VERSION"\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml
  ```

### 2. Python-Skript ausführen
1. Bearbeite den Pfad zur Haarcascade-Datei im Python-Skript:
   ```python
   haarcascade_path = "C:/Pfad/haarcascade_frontalface_default.xml"
   ```
2. Starte das Gesichtserkennungs-Skript (Terminal/Kommandozeile/Eingabeaufforderung):
   ```bash
   python face_recognition.py
   ```

3. Binde den ESP32-Videostream ein:
   - Nutze die ESP32-IP-Adresse: `http://<IP>:81/stream`.

4. Lass das Skript erkannte Gesichter speichern und im Zielordner ablegen.

---

## Dateien und Ordnerstruktur

- **/src**
  - `face-recognition.py`: Python-Skript für die Gesichtserkennung.
  - `camera_pins.h`: Pin-Definitionen für ESP32-CAM.
  - `app_httpd.cpp`: Implementierung des Kamera-Webservers.
- **/data**
  - `haarcascade_frontalface_default.xml`: Haarcascade-Datei für OpenCV.
