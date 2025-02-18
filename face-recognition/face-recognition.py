import cv2
import os
import numpy as np
from datetime import datetime

#"USER"&"PYTHONVERSION abändern"
# Pfad zur Haar-Cascade-Datei
haar_cascade_path = "C:\\Users\\"USER"\\AppData\\Local\\Programs\\Python\\"PYTHON+VERSION"\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"

# Lade den Haar-Cascade-Classifier
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

if face_cascade.empty():
    print("Fehler: Haar-Cascade-Datei konnte nicht geladen werden!")
    exit()

# Ordner für gespeicherte Gesichter
faces_dir = "faces"
os.makedirs(faces_dir, exist_ok=True)

# Gespeicherte Gesichter laden
def load_known_faces():
    known_faces = {}
    for file in os.listdir(faces_dir):
        if file.endswith(".jpg"):
            img = cv2.imread(os.path.join(faces_dir, file))
            person_name = file.split("_")[0]
            if person_name not in known_faces:
                known_faces[person_name] = []
            known_faces[person_name].append(img)
    return known_faces

# Gesicht erkennen
def recognize_face(face_img, known_faces):
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    for name, images in known_faces.items():
        for stored_img in images:
            stored_gray = cv2.cvtColor(stored_img, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(gray, stored_gray, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)
            if max_val > 0.7:  # Schwellenwert für Ähnlichkeit
                return name
    return None

# Funktion zur Verarbeitung des ESP32-CAM-Streams (ohne neue Speicherung)
def process_stream_without_saving(stream_url):
    known_faces = load_known_faces()
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print(f"Fehler: Stream von {stream_url} konnte nicht geöffnet werden!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fehler: Kein Frame erhalten!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            recognized_name = recognize_face(face_img, known_faces)

            if recognized_name:
                print(f"Bekanntes Gesicht erkannt: {recognized_name}")
                cv2.putText(frame, recognized_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                print("Unbekannte Person erkannt.")
                cv2.putText(frame, "Unbekannte Person", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("ESP32-CAM Gesichtserkennung (ohne Speicherung)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Funktion zur Verarbeitung des ESP32-CAM-Streams (mit Speicherung)
def process_stream_with_saving(stream_url):
    known_faces = load_known_faces()
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print(f"Fehler: Stream von {stream_url} konnte nicht geöffnet werden!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fehler: Kein Frame erhalten!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            recognized_name = recognize_face(face_img, known_faces)

            if recognized_name:
                print(f"Bekanntes Gesicht erkannt: {recognized_name}")
                cv2.putText(frame, recognized_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                print("Neues Gesicht erkannt. Bitte speichern.")
                save_new_face(face_img)
                known_faces = load_known_faces()

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("ESP32-CAM Gesichtserkennung (mit Speicherung)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Gesicht speichern
def save_new_face(face_img):
    person_name = input("Neues Gesicht erkannt. Bitte Namen eingeben: ")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    face_path = os.path.join(faces_dir, f"{person_name}_{timestamp}.jpg")
    cv2.imwrite(face_path, face_img)
    print(f"Neues Gesicht unter {person_name} gespeichert.")

# Hauptprogramm
if __name__ == "__main__":
    print("Optionen:")
    print("1: Lokales Bild verarbeiten")
    print("2: ESP32-CAM Stream verarbeiten (mit Speicherung)")
    print("3: ESP32-CAM Stream verarbeiten (ohne Speicherung)")
    option = input("Wähle eine Option (1/2/3): ")

    if option == "1":
        image_path = input("Pfad zum Bild eingeben: ")
        process_image(image_path)
    elif option == "2":
        stream_url = input("ESP32-CAM Stream-URL eingeben (z.B. http://192.168.178.123:81/stream): ")
        process_stream_with_saving(stream_url)
    elif option == "3":
        stream_url = input("ESP32-CAM Stream-URL eingeben (z.B. http://192.168.178.123:81/stream): ")
        process_stream_without_saving(stream_url)
    else:
        print("Ungültige Option!")