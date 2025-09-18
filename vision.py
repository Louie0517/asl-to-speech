import cv2
from ultralytics import YOLO
from gtts import gTTS
from playsound import playsound
import tempfile
import os

model = YOLO(r"C:\CompVision\runs\detect\train4\weights\best.pt")


def speak_text(text):
    if not text.strip():
        return  
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)
    playsound(temp_path)
    os.remove(temp_path)

cap = cv2.VideoCapture(0)

sentence_buffer = ""
current_label = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  
    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            current_label = label  

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 192, 203), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    cv2.putText(frame, f"Buffer: {sentence_buffer}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("ASL to Speech", frame)

    key = cv2.waitKey(1) & 0xFF
    # Exit
    if key == ord('e'):  
        break
    # SPACE adds a space
    elif key == 32:  
        sentence_buffer += " "
        # ENTER speaks the buffer
    elif key == 13:  
        print("Speaking:", sentence_buffer)
        speak_text(sentence_buffer)
        sentence_buffer = ""
        # Press 's' to store current detected letter
    elif key == ord('s'):  
        if current_label != "":
            sentence_buffer += current_label
            print("Buffer:", sentence_buffer)
        # Backspace/Delete 
    elif key == 8:
        if len(sentence_buffer) > 0:
            sentence_buffer = sentence_buffer[:-1]
            print("Buffer after delete:", sentence_buffer)

cap.release()
cv2.destroyAllWindows()
