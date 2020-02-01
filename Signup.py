from tkinter import *
import pandas as pd
from tkinter.messagebox import *
import os

tk = Tk()
tk.title('Signup')

#Variables being used for details
user1 = StringVar()
pass1 = StringVar()


image = PhotoImage(file="NGNL.gif")
tk.geometry('830x730')
label = Label(image=image,pady=200)


def Back():
    os.system('Login.py')

#Function to add the Valid Users

def Enter():
    x='@ # $ % ^ & * !'.split()
    for i in x:
        if i in pass1.get():
            df1=pd.read_csv('User_detail.csv')
            df2=pd.DataFrame({'Username':user1.get(),'Password':pass1.get()},index=[df1.index[-1]+1])
            df1=pd.concat([df1,df2],ignore_index=True)
            with open('User_detail.csv','w') as f:
                df1.to_csv(f, header=True)
            showinfo('Signup','User added successfully')
            break
        elif i=='!':
            showinfo('Validation',"1.Password must contain atleast one Captial character \n2.Password must contain either of '@#$%^&*!'")

username = Label(tk, text="Username",fg='green',bg='black',pady=10)
username1 = Entry(tk, textvariable=user1, bd=2, fg='green',bg='black')
password = Label(tk, text="Password",fg='green',bg='black',pady=10)
password1 = Entry(tk, textvariable=pass1, show="*", bd=2,fg='green',bg='black')
valid = Label(tk,fg='green',bg='black', text="1.Password must contain atleast one Captial character\n2.Password must contain either of '@#$%^&*!'")
Enter=Button(tk, text='Enter', command=Enter,fg='green',bg='black')
Back=Button(tk, text='Back', command=Back,fg='green',bg='black')

label.place(width=1200, height=800, x=-180, y=0)
username.place(width=100, height=20, x=550, y=200)
username1.place(width=100, height=20, x=650, y=200)
password.place(width=100, height=20, x=550, y=240)
password1.place(width=100, height=20, x=650, y=240)
Enter.place(width=60, height=20, x=620, y=280)
valid.place(width=300, height=40, x=510, y=310)
Back.place(width=60, height=20, x=700, y=280)

tk.mainloop()
