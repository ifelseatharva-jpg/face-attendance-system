import os
import cv2
import pandas as pd
import datetime

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWN_FACES_DIR = os.path.join(BASE_DIR, "data", "known_faces")
OUTPUT_CSV = os.path.join(BASE_DIR, "data", "attendance.csv")

# --- Load Haar Cascade ---
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# --- Initialize attendance list ---
attendance = []

# --- Load existing attendance if CSV exists ---
if os.path.exists(OUTPUT_CSV):
    df_existing = pd.read_csv(OUTPUT_CSV)
    today = datetime.date.today()
    attendance = df_existing[df_existing["Date"] == str(today)].values.tolist()

# --- Function to mark attendance ---
def mark_attendance(name):
    if name not in [entry[0] for entry in attendance]:
        time_now = datetime.datetime.now()
        attendance.append([name, time_now.date(), time_now.strftime("%H:%M:%S")])
        print(f"✅ Attendance marked: {name} at {time_now.strftime('%H:%M:%S')}")

# --- OFFLINE MODE: Scan images in known_faces folder ---
def offline_mode():
    if not os.path.exists(KNOWN_FACES_DIR):
        raise FileNotFoundError(f"Folder not found: {KNOWN_FACES_DIR}")

    for file in os.listdir(KNOWN_FACES_DIR):
        img_path = os.path.join(KNOWN_FACES_DIR, file)
        name = os.path.splitext(file)[0]

        # Skip if already marked today
        if name in [entry[0] for entry in attendance]:
            continue

        img = cv2.imread(img_path)
        if img is None:
            print(f"Skipping unreadable image: {img_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            mark_attendance(name)

# --- ONLINE MODE: Laptop webcam ---
def laptop_webcam_mode():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("⚠️ Laptop webcam not detected!")
        return

    print("🎥 Press 'q' to quit laptop webcam mode.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Laptop Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# --- ONLINE MODE: Phone webcam via IP Webcam ---
def phone_webcam_mode():
    url = input("Enter your phone IP Webcam URL (e.g., http://192.168.1.5:8080/video): ").strip()
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("⚠️ Failed to connect to phone webcam!")
        return

    print("🎥 Press 'q' to quit phone webcam mode.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame from phone!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Phone Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# --- User chooses mode ---
print("Choose mode:\n1 - Offline (folder images)\n2 - Laptop webcam\n3 - Phone webcam (IP Webcam)")
mode = input("Enter 1, 2, or 3: ").strip()

if mode == "1":
    offline_mode()
elif mode == "2":
    laptop_webcam_mode()
elif mode == "3":
    phone_webcam_mode()
else:
    print("⚠️ Invalid option selected!")

# --- Save attendance ---
df = pd.DataFrame(attendance, columns=["Name", "Date", "Time"])
df.to_csv(OUTPUT_CSV, index=False)
print("✅ Attendance saved successfully!")
