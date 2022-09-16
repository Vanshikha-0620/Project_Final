#opencv-contrib-python
#opencv-python
#numpy
#cvzone
#Pillow-PIL
#Pillow

from tkinter import *

import cv2
from PIL import  Image, ImageTk
import os
import threading

def __ma__():
    filename = 'main.py'
    os.system(filename)
    os.system('notepad'+filename)

def __ve__():
    filename = 'vehicle.py'
    os.system(filename)
    os.system('notepad'+filename)

def __ex__():
    root.destroy()

root = Tk()
root.title("Detector")
root.iconbitmap(r'C:/Users/Sync/Desktop/PythonImg/parked-car.ico')
root.geometry('900x460')#+200+50
root.resizable(FALSE, FALSE)
title = Label(root, text="Parking Space Detector + Vehicle Counter", font=('Futura', 25),
              bg='#0a064f', fg='white')
title.place(x=0, y=0, relwidth=1)
frm = Frame(root, bd=0, relief=RIDGE, bg='white')

load=Image.open("C:/Users/Sync/Desktop/PythonImg/PC2.jpg")
render = ImageTk.PhotoImage(load)
img = Label( image = render)
img.place(x=0, y=40, width=450, height=420)

load1=Image.open("C:/Users/Sync/Desktop/PythonImg/VD4.jpg")
render1 = ImageTk.PhotoImage(load1)
img1 = Label( image = render1)
img1.place(x=450, y=40, width=450, height=420)


btn = Button(master=root, text='Parking Detection', font=('Futura', 10), bg='#326fa8', bd=5, fg='white', command = threading.Thread(target=__ma__).start)
btn.place(x=150,y=400)

btn2 = Button(root, text='Vehicle Detection',font=('Futura', 10), bg='#326fa8', bd=5, fg='white', command = threading.Thread(target=__ve__).start)
btn2.place(x=600,y=400)

btn3 = Button(root, text="Exit", font=('Futura', 10), bg='#326fa8', bd=5, fg='white', command =__ex__)
btn3.place(x=430,y=400)

root.mainloop()

