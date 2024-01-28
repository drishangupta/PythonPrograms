import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import os
cap = cv2.VideoCapture(0)
modelH = HandDetector()
while True:
        status , photo = cap.read()
        photo1=modelH.findHands(photo)
        photo1[1]
        cv2.imshow("hi", photo1[1])
        if cv2.waitKey(100) == 13:
            break
    
        hand = modelH.findHands(photo, draw=False)
        fingeruplist=[0,0,0,0,0]
        if hand:
            lmlist = hand[0]
            fingeruplist = modelH.fingersUp(lmlist)
            print(fingeruplist)
        if fingeruplist == [0 ,1 , 0, 0 , 0]: 
           os.system("start chrome")
            
           time.sleep(2)
        elif fingeruplist == [0 ,1 , 1, 0 , 0]: 
            
            os.system("firefox") 
            time.sleep(2)
        elif fingeruplist == [0 ,1 , 1, 1 , 0]: 
            
            #Your Function here 
            time.sleep(2)
        elif fingeruplist == [0 ,1 , 1, 1 , 1]: 
            
            #Your Function here 
            time.sleep(2)
        elif fingeruplist == [1 ,1 , 1, 1 , 1]: 
            
            #Your Function here  
            time.sleep(2)