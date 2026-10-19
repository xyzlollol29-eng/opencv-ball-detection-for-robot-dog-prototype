import cv2
import numpy as np

cap = cv2.VideoCapture(0)
bawlz_seen=False
while True:
    ret,frame= cap.read()
    if ret:
     cv2.line(frame, (frame.shape[1] //2,0), (frame.shape[1]//2,frame.shape[0]),(255,255,255),3)
     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower1 = np.array([0, 150, 150])
    upper1 = np.array([10, 255, 255])
    lower2 = np.array([170, 150, 150])
    upper2 = np.array([179, 255, 255])
    mask = cv2.inRange(hsv,lower1,upper1) | cv2.inRange(hsv,lower2,upper2)
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    if contours:
      if not bawlz_seen:
         print("woof")
         bawlz_seen=True
      biggest =max(contours,key=cv2.contourArea)
      if cv2.contourArea(biggest)>300:
            (x,y),radius=cv2.minEnclosingCircle(biggest)
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,0),2)
            if int(x) <int(frame.shape[1] //2):
              print("left")
            else:
              print("right")
    
    cv2.imshow("Ball", frame)
               # cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
            
cap.release()
cv2.destroyAllWindows()
