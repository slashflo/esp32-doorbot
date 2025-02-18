### Unterrichtseinheit: Steuerung eines ESP32 über einen Telegram Bot
---
### **Arbeitsblatt**

#### **Aufgabe 1: Bot erstellen, API-Schlüssel und Chat-ID einrichten**
**1a. Telegram Chat-Bot erstellen**
1. Öffne den Telegram Tab im Browser und interagiere mit dem Chat des Bot-Fathers. 
2. Erstellt nun einen neuen Bot und gebt ihm einen aussagekräftigen Namen.
3. Fügt den Bot einer Chat Gruppe hinzu oder kommuniziere direkt mit ihm.
    
**1b. API-Schlüssel eintragen**
1. Öffne den bereitgestellten Code für den ESP32 in der Arduino IDE (telegram-led.ino).
2. Analysiert den Code grob. Was stellt dieser bereit und wie funktioniert es?
3. Suche nach der Stelle, an der der API-Schlüssel eingefügt werden muss und tragt diesen ein.
4. Teste den Bot, indem du die Befehle in der Telegram Gruppe versendest. Was fällt euch auf? 

**Wendet euch nach Abschluss dieser Aufgabe wieder an euren Betreuer.**

**1c. Chat-ID auslesen**
1. Schalte den ESP32 aus.
2. Rufe den folgenden Endpoint des Telegram Bots im Browser auf:
   ```
   https://api.telegram.org/bot123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ/getUpdates
   ```
4. Sende über Telegram eine Nachricht an den Bot.
5. Aktualisiere die Seite und finde deine Chat-ID in der JSON-Antwort.
   ```
   {
       "update_id": 123456789,
       "message": {
           "chat": {
               "id": 987654321,
               ...
           }
       }
   }
   ```
7. Trage die Chat-ID im Code ein:
8. Teste die Botfunktionen nun erneut.

---

#### **Aufgabe 2: Zusätzliche Befehle implementieren**
1. Überlege dir weitere Befehle, die du dem Bot hinzufügen könntest (z. B. LED kurz aufleuchten lassen o.ä.)
2. Füge die neuen Befehle in den entsprechenden Abschnitt des Codes ein:
3. Teste die neuen Funktionen.
4. *Optional:* Verändere die Funktionen (/led_on & /led_off) so, dass der Befehl nur ausgeführt werden kann, falls der Status der LED richtig ist.
Bspw. soll eine Fehlermeldung ("LED ist bereits ausgeschaltet") erscheinen falls die LED bereits ausgeschaltet ist und der Befehl /led_off erneut gesendet wurde.

---

#### **Aufgabe 3: Kamera des ESP32 ansteuern (BONUS)** 
#### **3a. Code vorbereiten und verstehen**  
1. Öffne das Beispiel CameraWebServer in der Arduino IDE: Datei → Beispiele → ESP32 → Camera → CameraWebServer.

<img width="976" alt="Screenshot 2025-02-18 at 15 37 09" src="https://github.com/user-attachments/assets/3e05ed0f-fc9f-48b8-9f19-416586d8cc93" />

2.Passe folgende Einstellungen im Code an:
Wähle das richtige Board (z. B. AI Thinker ESP32-CAM).

<img width="894" alt="Screenshot 2025-02-18 at 15 42 10" src="https://github.com/user-attachments/assets/13e3f524-9627-4211-b126-69cfc65c0fff" />

3. Öffne den bereitgestellten Code für den ESP32 in der Arduino IDE (`telegram-cam.ino`).  
4. Lies den Code (Methodennamen) und verschaffe dir einen Überblick über die Funktionalität.  
5. Starte den Code auf dem ESP32, um sicherzustellen, dass er korrekt hochgeladen wird.  

---

#### **3b. Befehle testen und verstehen**  
1. Öffne die Telegram-App und interagiere mit dem erstellten Bot.  
2. Teste den Befehl `/photo` und überprüfe, ob der Bot erfolgreich ein Foto aufnimmt und sendet.  
3. Beobachte die Reaktion des ESP32 auf diesen Befehl:  
   - Welche LED blinkt?  
   - Wie lange dauert die Übertragung des Fotos?  

---

#### **3c. Funktionen des Codes nachvollziehen**  
1. Suche im Code die Stelle, an der der `/photo`-Befehl verarbeitet wird.  
2. Versuche, die folgenden Fragen zu beantworten:  
   - Welches Kameramodul wird verwendet?  
   - Wie wird das Foto aufgenommen? (Welche Funktion wird dafür aufgerufen?)  
   - Wie wird das Foto an den Telegram-Chat gesendet?  

---
