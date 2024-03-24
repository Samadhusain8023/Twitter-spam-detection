import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.font as font
from tkinter import filedialog
import tkinter.messagebox as tm
import Preprocess as pr
import CreateDataset as cd
import KNNALG as knn
import NBALG as nb
import LRALG as lr
import SVMALG as svm
from tkinter import ttk



from_date = datetime.datetime.today()
currentDate = time.strftime("%d_%m_%y")

fontScale=1
fontColor=(0,0,0)
cond=0

bgcolor="#a05887"
fgcolor="white"

window = tk.Tk()
window.title("Twitter Spam Drift")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message1 = tk.Label(window, text="Twitter Spam Drift" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=10)

lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=10, y=200)

txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=300, y=215)




def clear():
	txt.delete(0, 'end') 

def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.delete(0, 'end') 
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")	

def preprocess():
	sym=txt.get()
	if sym != "" :
		pr.process(sym)
		res = "Preprocess Finished Successfully"
		tm.showinfo("Input", "Preprocess Finished Successfully")
	else:
		tm.showinfo("Input error", "Select Dataset")

	

def createdataset():
	cd.process()
	tm.showinfo("Input", "DataSet Created Successfully")


def svmprocess():
	svm.process()
	tm.showinfo("Input", "SVM Finished Successfully")

def nbprocess():
	nb.process()
	tm.showinfo("Input", "Navy Base Finished Successfully")

def knnprocess():
	knn.process()
	tm.showinfo("Input", "KNN Finished Successfully")
		

def lrprocess():
	lr.process()
	tm.showinfo("Input", "LogisticRegression Finished Successfully")
		
clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=960, y=200)

browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=530, y=205)

pre1 = tk.Button(window, text="CreateDataset", command=createdataset  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
pre1.place(x=10, y=600)


pre = tk.Button(window, text="Preprocess", command=preprocess ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
pre.place(x=190, y=600)

texta = tk.Button(window, text="NavyBase", command=nbprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta.place(x=370, y=600)

texta1 = tk.Button(window, text="LogisticRegression", command=lrprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta1.place(x=550, y=600)

texta1 = tk.Button(window, text="KNN", command=knnprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta1.place(x=740, y=600)

texta1 = tk.Button(window, text="SVM", command=svmprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta1.place(x=910, y=600)


quitWindow = tk.Button(window, text="QUIT", command=window.destroy  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1080, y=600)

 
window.mainloop()
