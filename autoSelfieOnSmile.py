import cv2
import datetime
# import png
# cap=cv2.VideoCapture(0)
def AutoSelfie():
    cap=cv2.VideoCapture(0)
    cascade="F:\\python\\cascade\\haarcascade_frontalface_default.xml"
    cascade1="F:\\python\\cascade\\haarcascade_smile.xml"

    face_cascade=cv2.CascadeClassifier(cascade)
    smile_cascade=cv2.CascadeClassifier(cascade1)
    while True:
        _,frame=cap.read()
        original_frame=frame.copy()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray, 
                                 scaleFactor=1.3, 
                                 minNeighbors=5)
        for x,y,w,h in  face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            face_roi=frame[y:y+h,x:x+w]
            gray_roi=gray[y:y+h,x:x+w]
            smile=smile_cascade.detectMultiScale(gray_roi,1.3,25)
            for x1,y1,w1,h1 in  smile:
                cv2.rectangle(face_roi,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)
                time_stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                fileName=f'selfie-{time_stamp}.png'
                cv2.imwrite(fileName,original_frame)
        cv2.imshow('Cam Start',frame)
        if cv2.waitKey(10)==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()




