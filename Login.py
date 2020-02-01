from tkinter import *
#from PIL import ImageTk, Image
import os
import pandas as pd
from tkinter.messagebox import *

tk = Tk()
tk.configure(background = 'black')
tk.title('Tic Tac Toe')

#Image_path=r"1_81GhGbn6cnJycDP92rBDqQ.gif"  # Enter the path of image file.


image = PhotoImage(file=r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\NGNL.gif")
tk.geometry('830x730')
label = Label(image=image,pady=200)


df1=pd.read_csv('User_detail.csv')

#Variables being used for details
user1 = StringVar()
pass1 = StringVar()

#functions to open different screen
def Signup():
    os.system('Signup.py')
    
def Validate():
    if df1.index[df1['Username']==user1.get()] == df1.index[df1['Password']==pass1.get()]:
        os.system('check1.py')
    else:
        showinfo('Signup','Invalid User')

#Main GUI design
username = Label(tk, text="Username",fg='green',bg='black',pady=10)
username1 = Entry(tk, textvariable=user1, bd=2, fg='green',bg='black')
password = Label(tk, text="Password",fg='green',bg='black',pady=10)
password1 = Entry(tk, textvariable=pass1, show="*", bd=2,fg='green',bg='black')
Login=Button(tk, text='Login', command=Validate,fg='green',bg='black',pady=10)
Signup=Button(tk, text='Signup',command=Signup,fg='green',bg='black',pady=10)


label.place(width=1200, height=800, x=-180, y=30)
username.place(width=100, height=20, x=550, y=200)
username1.place(width=100, height=20, x=650, y=200)
password.place(width=100, height=20, x=550, y=240)
password1.place(width=100, height=20, x=650, y=240)
Login.place(width=50, height=20, x=650, y=270)
Signup.place(width=50, height=20, x=720, y=270)
tk.mainloop()
