from tkinter import *
from tkinter import messagebox
import os
import pandas as pd

top = Tk()
top.configure(background = 'skyblue')
#title of the project
top.title('Home')

global count
count = 0


title = Label(top,text = 'TIC - TAC - TOE',bg = 'blue',fg = 'white',font = 'Times 50 bold italic').grid(row = 1,column = 3)

def one_player():
    os.system('one.py')

def two_player():
    os.system('two.py')

def exi():
    e = messagebox.askyesno('Confirm','Do you want to exit')
    if e > 0:
        top.destroy()
        return

#To clear the rules label
def rule():
    rule = "1. The game is played on a grid that \'s \n    3 squares by 3 squares.\n\
2. You are X, your friend (or the computer in this case) is O.\n  Players take turns putting their marks in empty squares.\n\
3. The first player to get 3 of her marks in a row \n   (up, down, across, or diagonally) is the winner.\n\
4. When all 9 squares are full, the game is over.\n   If no player has 3 marks in a row, the game ends in a tie.\n "
    messagebox.showinfo('How to play?',rule)
        


global z
z = 0
def show():
    global z
    found = 0
    player = name.get()
    data = pd.read_csv('c.csv')
    for z in range(0,len(data)):
        if data['name'][z] == player:
            found = found + 1
            break;

    if found == 0:
        messagebox.showinfo('Error','Invalid Username')
        return
    else:      
        score_rec = 'MATCHES PLAYED - ' + str(data['played'][z]) + '  MATCHES WON - ' + str(data['win'][z]) + '  MATCHES LOSE - ' + str(data['lose'][z]) + ' TIE - ' + str(data['tie'][z])
        score_card = Label(top,text = score_rec,bg = 'blue',fg = 'white',font = 'Times 15 bold italic').grid(row = 5,column = 1,columnspan = 6)

name = StringVar()
global more_one
more_one = 0
def score():
    global more_one
    if more_one == 1:
        return 1
    data = pd.read_csv('c.csv')
    global show
    user = Label(top,text = 'USER NAME').grid(row = 6,column = 3)
    get = Entry(top,textvariable = name).grid(row = 7,column = 3)
    show = Button(top,text = 'Show',command = show).grid(row = 8,column = 3)
    more_one += 1


photo = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\index.png")
photoimage = photo.subsample(1,1)
    
    
    
    

#BUTTONS IN THE HOME PAGE
one_player = Button(text = 'SINGLE PLAYER',bg = 'black',fg = 'white',activebackground= 'pink',activeforeground = 'red',font = 'Times 25 bold',width = 20,command = one_player).grid(column= 2, row=2,padx = 20,pady = 50)
two_player = Button(text = 'TWO PLAYER',bg = 'black',fg = 'white',activebackground= 'pink',activeforeground = 'red',font = 'Times 25 bold',width = 20,command = two_player).grid(column= 4, row=2,padx = 20,pady = 50)
score = Button(text = 'SCORE CARD',bg = 'black',fg = 'white',activebackground= 'pink',activeforeground = 'red',font = 'Times 25 bold',width = 20,command = score).grid(column= 2, row=3,padx = 20,pady = 50)
rules = Button(text = 'HOW TO PLAY?',bg = 'black',fg = 'white',activebackground= 'pink',activeforeground = 'red',font = 'Times 25 bold',width = 20,command = rule).grid(column= 4, row=3,padx = 20,pady = 50)
exit = Button(text = 'EXIT',bg = 'black',fg = 'white',activebackground= 'pink',activeforeground = 'red',font = 'Times 25 bold',width = 20,command = exi).grid(column= 3, row=4,padx = 20,pady = 50)




#c = Button(text = 'close',command = hide).grid(column= 1, row=5)
can = Label(top,bg = 'white',image = photoimage)
can.grid(column = 3,row = 2,rowspan = 2,padx = 30,pady = 20)

top.mainloop()
    
