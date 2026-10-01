import cv2

#-m pip uninstall opencv-python opencv-contrib-python opencv-python-headless -y
#pip install opencv-python==4.10.0.84
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Error: camera could not open')
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("failed to capture image")
        break

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=5, minSize=(30, 30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f'People count: {len(faces)}', (10,30), font, 1, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow('Face tracking and Counting', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()