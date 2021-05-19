import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Video web cam input
# cap = cv2.VideoCapture(0)

# mp4
cap = cv2.VideoCapture('face.mp4')
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Face detection
    face = face_cascade.detectMultiScale(gray, 1.1, 4)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
