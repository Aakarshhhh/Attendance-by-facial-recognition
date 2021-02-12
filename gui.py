import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from datetime import datetime
global sn
sn=0
root= tk.Tk()
root.title('Cyber Ninja Systems')
now = datetime.now()
canvas1 = tk.Canvas(root,width = 400, height = 300,  relief = 'raised')
canvas1['bg'] = 'black'
canvas1.pack()

label1 = tk.Label(root, text='Facial Recognition Attendance System',bg='black', fg='white')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter your Roll Number:',bg='black', fg='white')
label2.config(font=('helvetica', 10))
canvas1.create_window(80, 100, window=label2)
label3 = tk.Label(root, text='Enter your Name:',bg='black', fg='white')
label3.config(font=('helvetica', 10))
canvas1.create_window(62, 160, window=label3)

entry1 = tk.Entry (root) 
entry2 = tk.Entry (root) 
canvas1.create_window(230, 100, window=entry1)
canvas1.create_window(230, 160, window=entry2)
def getdata ():
    state=0
    global sn
    x1= entry1.get()
    name= entry2.get()
    import reco
    trans={"CI190082":0,"CI190083":1,"CI190084":2,"CI190085":3,"CI190086":4,"CI190087":5,"CI190088":6,"CI190076":7,"CI190077":8}
    
    state=reco.labeltrans(trans[x1],name)
    if state==0:
        label1 = tk.Label(root,text="                                      Try Again                                     ",bg='black', fg='white',font=('helvetica', 12))
        canvas1.create_window(200, 210, window=label1)
    if state==10:
        label1 = tk.Label(root, text= x1 +" "+ name +" Marked Present",bg='black', fg='white',font=('helvetica', 12))
        canvas1.create_window(200, 210, window=label1)
        sn=sn+1
        with open('Attendance.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            if sn==1:
                writer.writerow(["S.No.","Roll No. ", "Name ", "Date and Time"])
            writer.writerow([sn,x1,name,now])
button1 = tk.Button(text='Click For Attendance ', command=getdata,bg='white', fg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 280, window=button1)

root.mainloop()
