import cv2
facCascade= cv2.CascadeClassifier("image processing with python\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    damn, img=cap.read()
    faces=facCascade.detectMultiScale(img,2,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("img",img)
        k=cv2.waitKey(30) & 0xFF==ord('d')
