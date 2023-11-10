import threading
import cv2
from deepface import DeepFace



#To capture the users face
cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)


#Frame in which the image is captured
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False


#Reference image used to match the live face
reference_img1 = cv2.imread("WIN_20231110_11_19_20_Pro.jpg")


#Checking whether the face is a match or not
def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img1.copy())['verified']:
            face_match = True
        else:
            face_match = False

    except ValueError:
        face_match = False


#Scans upto 30 frames and matches the face
while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
#If face matches then gives name as output
        if face_match:
            cv2.putText(frame, "HI BHAVIN!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (2, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (2, 255, 0), 3)

        cv2.imshow("video", frame)
    key = cv2.waitKey(1)

#'q' is used to stop the live video
    if key == ord("q"):
        break

cv2.destroyAllWindows()
