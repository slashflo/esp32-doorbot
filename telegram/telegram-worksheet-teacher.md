# Unterrichtseinheit: Steuerung eines ESP32 über einen Telegram Bot

## Lernziel

Die Schüler sollen verstehen, wie eine API funktioniert, deren Schlüssel in einem Programm verwendet werden, und wie der ESP32 über einen Telegram Bot gesteuert werden kann.

---

### **Arbeitsblatt mit Lösungen und erweiterter Aufgabenbeschreibung**

#### **Aufgabe 1: Bot erstellen, API-Schlüssel und Chat-ID einrichten**

**1a. Telegram Chat-Bot erstellen**

1. Öffne den Telegram Tab im Browser und interagiere mit dem Chat des Bot-Fathers.

2. Erstelle nun einen neuen Bot und gib ihm einen aussagekräftigen Namen.
3. Fügt den Bot folgender Chat-Gruppe hinzu oder lasst ihn durch einen Lehrer hinzufügen.

<details>
<summary>Lösungen mit Anleitung</summary>

1. Öffne die Telegram-App.
2. Suche nach dem Bot "@BotFather" und starte eine Unterhaltung.
3. Sende den Befehl `/newbot`.
4. Gib deinem Bot einen Namen und einen eindeutigen Benutzernamen (muss auf `bot` enden).
5. Notiere dir den API-Token, den BotFather bereitstellt. Dies wird für die Programmierung benötigt.

</details>
<br />

**1b. API-Schlüssel eintragen**

1. Öffne den bereitgestellten Code für den ESP32 in der Arduino IDE (telegram-led.ino).

2. Analysiert den Code grob. Was stellt dieser bereit und wie funktioniert es?
3. Suche nach der Stelle, an der der API-Schlüssel eingefügt werden muss und tragt diesen ein.
4. Teste den Bot, indem du die Befehle in der Telegram Gruppe versendest. Was fällt euch auf?

<details>
<summary>Lösungen mit Anleitung</summary>

1. Code in Arduino IDE öffnen
2. Code analysieren
3. Api Schlüssel einfügen
4. Bot testen

</details>
<br />

------
**Optionale Durchführung eines kurzen Info Blockes zu API im Dialog mit den Schülern**
<details>
<summary>Erklärung von API</summary>

#### Fragen und Antworten

- Was ist eine API und wofür steht API?
- Wo habt ihr schonmal Kontakt mit einer API gehabt (wissentlich/unwissentlich) ?
- Warum sind API-Schlüssel wichtig, und was könnte passieren, wenn sie öffentlich zugänglich wären?
- Was bedeutet „Request“ und „Response“ in der Kommunikation mit einer API?
  
#### **Was ist eine API?**

- API steht für "Application Programming Interface".
- Ermöglicht die Kommunikation zwischen verschiedenen Software-Anwendungen.
- Beispiele im Alltag:
  - Wetter-Apps, die Daten von Wetterdiensten abrufen.
  - Bezahlung per PayPal in Online-Shops.
- Wichtige Begriffe:
  - **Endpoint**: Die URL, über die eine API angesprochen wird.
  - **API-Schlüssel**: Authentifizierungsmerkmal zur Nutzung einer API.
  - **Request** und **Response**: Anfrage und Antwort zwischen Client und Server.

</details>
<br />

-------

**1c. Chat-ID auslesen**

1. Schalte den ESP32 aus.

2. Rufe den folgenden Endpoint des Telegram Bots im Browser auf:

   ```
   https://api.telegram.org/bot123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ/getUpdates
   ```

3. Sende über Telegram eine Nachricht an den Bot.
4. Aktualisiere die Seite und finde deine Chat-ID in der JSON-Antwort.

   <details>
     <summary>Beispiel:</summary>

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

   </details>
   <br \>

5. Trage die Chat-ID im Code ein:
6. Teste die Botfunktionen nun erneut.

<details>
<summary>Lösungen mit Anleitung</summary>

1. Stromzufuhr zum ESP32 entfernen
2. URL im Browser aufrufen, hierbei muss der API-Schlüssel an der Stelle ``` bot123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ ``` in der URL eingesetzt werden.
3. Nachricht an den Bot senden.
4. Chat-ID auslesen (Screenshot hinzufügen)
5. CHAT ID im Code an der Stelle """ eintragen.
6. Bot Funktionen erneut testen.

</details>
<br />

---

#### **Aufgabe 2: Zusätzliche Befehle implementieren (WIP)**

1. Überlege dir weitere Befehle, die du dem Bot hinzufügen könntest (z. B. LED ausschalten).

2. Füge die neuen Befehle in den entsprechenden Abschnitt des Codes ein:

   ```
    if (text == "/led_off") {
       digitalWrite(LED_BUILTIN, LOW);
       bot.sendMessage(chat_id, "LED ist aus");
     }
   ```

3. Teste die neuen Funktionen.

---

#### **Aufgabe 3: Kamera des ESP32 ansteuern (BONUS)**  

Die folgenden Teilaufgaben sind für Lehrer gedacht, um die Aufgabenstellung und die dazugehörige Lösung besser zu verstehen:  

#### **3a. Code vorbereiten und verstehen**  

1. Öffne das Beispiel CameraWebServer in der Arduino IDE: Datei → Beispiele → ESP32 → Camera → CameraWebServer.

<img width="976" alt="Screenshot 2025-02-18 at 15 37 09" src="https://github.com/user-attachments/assets/3e05ed0f-fc9f-48b8-9f19-416586d8cc93" />

2.Passe folgende Einstellungen im Code an:
Wähle das richtige Board (z. B. AI Thinker ESP32-CAM).

<img width="894" alt="Screenshot 2025-02-18 at 15 42 10" src="https://github.com/user-attachments/assets/13e3f524-9627-4211-b126-69cfc65c0fff" />

3. Öffnen Sie den bereitgestellten Code `telegram-cam.ino` in der Arduino IDE.  
4. Der Code sollte die Telegram-Bibliothek, die Kamera-Bibliothek und die ESP32 Wi-Fi-Bibliothek einbinden. Prüfen Sie, ob die Methodennamen im Code den Schülern einen Überblick über die Funktionalität geben.  
5. Laden Sie den Code auf den ESP32 hoch, um sicherzustellen, dass die Hardware korrekt funktioniert (Kamera ist angeschlossen, WLAN-Verbindung besteht -> Das soll im Serial-Monitor bestätigt werden).  

---

#### **3b. Befehle testen und erklären**  

1. Starten Sie den Telegram-Bot und testen Sie die Funktionalität des `/photo`-Befehls. Sende `/photo`
2. Die Funktion `esp_camera_fb_get()` wird verwendet, um ein Bild vom Kamera-Modul zu erfassen.
Falls die Kamera kein Bild aufnehmen kann, wird der ESP32 neu gestartet
3. Was passiert bei /photo? Was sollten sie beachten?

Die Kamera nimmt ein Bild auf.
Das Bild wird in einem bestimmten Format (JPEG) codiert.
Über eine HTTP-POST-Anfrage wird das Bild an Telegram gesendet.

Prüfen Sie die Serial-Monitor-Ausgabe: Wenn der Server nicht erreichbar ist oder die Kamera kein Bild aufnimmt, wird eine Fehlermeldung ausgegeben.
Testen Sie den Befehl in der Telegram-App. Das Foto sollte im Chat erscheinen.

---

#### **3c. Funktionen im Code analysieren**  

Zeigen Sie den Schülern die Verarbeitung des `/photo`-Befehls im Code: Erarbeitung des /photo-Befehls:

1. Der /photo-Befehl wird im Bot-Framework erkannt und löst die Methode `sendPhotoTelegram()` aus. <br/>
2. Aufnahme eines Fotos: <br/>
Die Funktion `esp_camera_fb_get()` wird verwendet: <br/>

        camera_fb_t * fb = esp_camera_fb_get();

    fb ist ein Zeiger auf den Framebuffer des Kameramoduls. <br/>
    Wenn die Funktion fehlschlägt (fb == NULL), wird der ESP32 neu gestartet.

3. Senden des Fotos an Telegram: <br/>

    Der HTTP-POST-Request wird vorbereitet: <br/>
    Header: Enthält Informationen wie chat_id und den Dateinamen des Fotos.  

        String head = "--IotCircuitHub\r\nContent-Disposition: form-data; name=\"chat_id\";
        \r\n\r\n" + chatId + "\r\n--IotCircuitHub\r\nContent-Disposition: form-data; 
        name=\"photo\"; filename=\"esp32-cam.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n";

    Bilddaten: Die eigentlichen Bilddaten werden in Blöcken von 1024 Bytes gesendet:

        for (size_t n = 0; n < fbLen; n = n + 1024) {
            if (n + 1024 < fbLen) {
                client.write(fbBuf, 1024);
                fbBuf += 1024;
            } else if (fbLen % 1024 > 0) {
                size_t remainder = fbLen % 1024;
                client.write(fbBuf, remainder);
            }
        }

    Footer: Schließt die HTTP-Anfrage ab: <br/>

        String tail = "\r\n--IotCircuitHub--\r\n";

4. Verarbeitung der Serverantwort: <br/>
    Der ESP32 wartet auf die Antwort des Telegram-Servers: <br/>

        while (client.available()) {
            char c = client.read();
            if (c == '\n') {
                if (getAll.length() == 0) state = true;
                getAll = "";
            } else if (c != '\r') {
                getAll += String(c);
            }
            if (state == true) {
                getBody += String(c);
            }
            startTimer = millis();
        }

5. Fehlerbehandlung: <br/>
Bei Verbindungsproblemen oder anderen Fehlern wird eine entsprechende Fehlermeldung ausgegeben: <br/>

        if (!client.connect(myDomain, 443)) {
            getBody = "Connected to api.telegram.org failed.";
            Serial.println("Connected to api.telegram.org failed.");
        }

<br/>

---

#### **Abschluss**

- Diskussion
  - Welche Möglichkeiten bietet die Ansteuerung über eine API?
  - Welche Probleme können auftreten und wie können diese gelöst werden?
  - Was unterscheidet öffentliche APIs von privaten APIs?
  - Welche weiteren Funktionen würdet ihr einem Telegram Bot hinzufügen, wenn keine Grenzen gesetzt wären?
  - Wie könnte man die Kamera des ESP32 in zukünftige Projekte integrieren?
