
import cv2
from face_detector import detect_face
from face_recognizer import recognize_face
from mask_detector import detect_mask
from emotion_detector import detect_emotion
from utils import log_access
import datetime

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = detect_face(frame)

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            name = recognize_face(face_img)
            mask_status = detect_mask(face_img)
            emotion = detect_emotion(face_img)
            access = "YES" if mask_status == "Mask" else "NO"

            log_access(name, mask_status, emotion, access)

            label = f"{name}, Mask: {mask_status}, Emotion: {emotion}, Access: {access}"
            color = (0, 255, 0) if access == "YES" else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow("Smart Secure Access System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
