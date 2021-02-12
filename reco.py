import os
import cv2
import numpy as np
import faceRecognition as fr
from tkinter import messagebox
def labeltrans(x1,x2):
    x1=int(x1)
    ctr=0
    nctr=0
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainingData.yml')
    name={0:"Aakarsh Anubhav",1:"Soham Samanta",2:"Kondala Snehasis Rao",3:"Apurva Shahabadi",4:"Shivam Singh",5:"Kunwar Pratyush",6:"Harsh Anand",7:"Ch. Harika",8:"Maasid Zafar"}


    
    cap=cv2.VideoCapture(0)
    while ctr<=21:
        
        ret,test_img=cap.read()
        faces_detected,gray_img=fr.faceDetection(test_img)
        for (x,y,w,h) in faces_detected:
            cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),2)
        for face in faces_detected:
            (x,y,w,h)=face
            roi_gray=gray_img[y:y+w, x:x+h]
            label,confidence=face_recognizer.predict(roi_gray)
            #print("label:",label)
            fr.draw_rect(test_img,face)
            predicted_name=name[label]
            if confidence < 72:
                print(x1," ",ctr," ",nctr," ",label," ",confidence," ",predicted_name," ",x2)
                fr.put_text(test_img,predicted_name,x,y)
                if x1==label and x2==predicted_name:
                    ctr=ctr+1
                if ctr==10:
                   messagebox.showinfo('AKKI', 'Operation Successful')
                   cap.release()
                   cv2.destroyAllWindows()
                   return ctr
                if x1!=label or x2!=predicted_name:
                    nctr=nctr+1
                if nctr==10:
                    messagebox.showinfo('Akki', 'Operation unsucessful')
                    cap.release()
                    cv2.destroyAllWindows()
                    return 0
        cv2.imshow('Cyber Ninja System',test_img)
        
        k = cv2.waitKey(30) & 0xff    
        if k == 27 or ctr ==20 :
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    return