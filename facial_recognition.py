import cv2
import os

class FacialRecognition:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def capture_face(self, member_id):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('Capture Face', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                path = f"faces/{member_id}.jpg"
                cv2.imwrite(path, frame)
                break
        cap.release()
        cv2.destroyAllWindows()
        return path

    def verify_face(self, member_id):
        return os.path.exists(f"faces/{member_id}.jpg")