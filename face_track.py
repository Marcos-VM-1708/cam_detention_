
import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0) # não reconheceu minha camera
modulo = mp.solutions.face_detection
face_detection = modulo.FaceDetection()
show = mp.solutions.drawing_utils

while cam.isOpened():
    x, frame = cam.read()
    if not x:
        print("fafa")
        break

    faces = face_detection.process(frame)

    if faces.detections:
        for rosto in faces.detections:
            show.draw_detection(frame, rosto)

    cv2.imshow("Rostos na sua webcam", frame)

    if cv2.waitKey(5) == 27:
        break

cam.release()
cv2.destroyAllWindows()