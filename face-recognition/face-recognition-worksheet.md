Arbeitsblatt: ESP-32 Door-Bot mit Gesichtserkennung

Ziel: In diesem Arbeitsblatt richten wir einen ESP-32 als Door-Bot ein, führen eine Gesichtserkennung mit Python durch und lernen, wie die Bauteile zusammenarbeiten.
Teil 1: Vorbereitung

1.	Konsole öffnen:
  o	Öffne die Eingabeaufforderung oder das Terminal auf deinem PC.
2.	Python installieren:
  o	Lade Python von python.org herunter und installiere es.
3.	Prüfen, ob pip installiert ist:
  o	Gib im Terminal ein: 	pip—version
  o	Falls dies nicht der Fall ist gib das in die Konsole ein : pip install 

4.	Benötigte Bibliotheken installieren:
  o	Installiere OpenCV und NumPy:	py -m pip install opencv-python numpy
________________________________________
Teil 2: ESP-32 + CameraWebServer
	
1.	Installiere die Arduino IDE : 
  o	Gehe auf https://www.arduino.cc/en/software und lade dir die entsprechende Software für dein Betriebssystem herunter.

2.	Arduino IDE öffnen:
  o	Starte die Arduino IDE.

3.	CameraWebServer übernehmen:
  o	Öffne das Beispiel „CameraWebServer“:
      Datei → Beispiele → ESP32 → Camera → CameraWebServer

4.	Einstellungen im Code vornehmen:
  o	Ändere im Code:
    	#define ersetzen mit dem jeweiligen Modell, welches verwendet wird.
    	Board Manager auf das passende Modell anpassen.
  o	Ändere die SSID und das Passwort auf das verwendete Netzwerk.
  o	Stelle die Baudrate auf 115200 ein.

5.	Code hochladen:
  o	Schließe den ESP-32 an den PC an.
  o	Lade den Code hoch.

6.	Serial Monitor öffnen:
  o	Öffne den Serial Monitor in der Arduino IDE.
  o	Drücke den Reset-Knopf auf dem ESP-32.
  o	Notiere dir die angezeigte IP-Adresse.

7.	Camera_pins.h verstehen:
  o	Öffne die Datei camera_pins.h im Beispielprojekt.
  o	Diese Datei enthält die Pin-Konfiguration für verschiedene ESP-32-Modelle, die der Code verwendet, um die Kamera korrekt zu steuern.

8.	Kamera ausprobieren:

  o	Öffne die im Serial Monitor angezeigte IP-Adresse in deinem Browser.
  o	Teste die Kamera.
________________________________________

Teil 3: Gesichtserkennung mit Python

1.	Vorgefertigten Code verwenden:
  o	Öffne den Ordner mit dem vorbereiteten Python-Code (z. B. ein „face_recognition.py“-Skript).
  o	Bearbeite den Speicherort für die Haarcascade-Datei:
    	Standardpfad: C:\Users\"USER"\AppData\Local\Programs\Python\"PYTHON+VERSION"\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml

2.	Skript starten:
 o Starte das Gesichtserkennungs-Skript im Terminal: 	python face_recognition.py

3.	Videostream einbinden:
  o Verwende die ESP-32 IP-Adresse und den Videostream-Port: 	http://<IP>:81/stream

4.	Gesichter abspeichern:
  o	Lass das Skript Fotos der erkannten Gesichter machen und speichere diese mit passenden Namen.
  o	Lege einen Speicherordner für die Gesichter an und stelle sicher, dass dieser vom Skript genutzt wird.
________________________________________
Teil 4: Reflexion
Fragen:
1.	Was haben wir gelernt?



2.	Wie könnte die Gesichtserkennung im Gesamtprojekt eingebunden werden?

