from tkinter import *
from tkinter import messagebox
import random
import pandas as pd


tk = Tk()
tk.title("Tic Tac Toe")

frame = Frame(tk).grid()

#variables to take the usernames from Entry widgets
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

photo = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\killit.png")
photoimage = photo.subsample(1,1)

photox = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\comp.png")
photoimagex = photox.subsample(1,1)

photoy = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\comp_sad.png")
photoimagey = photoy.subsample(1,1)


photoz = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\person.png")
photoimagez = photoz.subsample(1,1)


photok = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\person_sad.png")
photoimagek = photok.subsample(1,1)

photot = PhotoImage(file = r"C:\Users\lenovo\Desktop\PYTHON_PROJECT\tie.png")
photoimaget = photot.subsample(1,1)




img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 10,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 11,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 12,padx = 0)

'''img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 11,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 12,padx = 0)'''

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=2, column=6, columnspan=8)
#state is disabled as this game is against computer
#player2_name = Entry(tk, textvariable=p2, bd=5,state = 'readonly') 
#player2_name.grid(row=3, column=6, columnspan=8)

#data variable contains previous values of data in csv 
data = pd.read_csv('c.csv')

#list 'a' is to append the clicked button numbers - which cannot be used further
a = []
#bclick is used to confirm the chance of user or computer
bclick = True
flag = 0
global present_check
present_check = 0
global index_of_player
index_of_player = 0



#disable all the buttons after game completed
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


c = 100
l = 100

global z
z = 0
def btnClick(buttons,i):
    global present_check,index_of_player,z
    
    global bclick, flag, player2_name, player1_name, playerb, pa,a,c,l
    found = 0
    z = 0
    l = 100
    c = 100
    player = p1.get()
    while z < len(data):
        if data['name'][z] == player:
            found = found + 1
            index_of_player = z
            break;
        else:
            z = z + 1
            #messagebox.showinfo('Error','Invalid Username')

    if found == 0:
        messagebox.showinfo('Error','Invalid Username')
        z = 0
        return
    #else:
     #   player1_name.configure(state = 'readonly')

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        playerb = "Computer Wins!"
        pa = p1.get() + " Wins!"
        get = checkForWin()
        if get == 1:
            return 0
        bclick = False
        flag += 1
        a.append(i)

    if bclick == False and (flag % 2 != 0):
        while True:
            k = random.randint(1,9)
            for j in a:
                if j == 5:
                    c = 0
                    break
                else:
                    c = c+1
            for j in a:
                if j == k:
                    l = 0
                    break
                else:
                    l = l + 1
            if (c != 0):
                button5['text'] = 'O'
                a.append(5)
                break
            elif l != 0:
                a.append(k)
                if k == 1 and button1['text'] != 'X':
                    button1['text'] = "O"
                    break
                elif k == 2 and button2['text'] != 'X':
                    button2['text'] = "O"
                    break
                elif k == 3 and button3['text'] != 'X':
                    button3['text'] = "O"
                    break
                elif k == 4 and button4['text'] != 'X':
                    button4['text'] = "O"
                    break
                elif k == 5 and button5['text'] != 'X':
                    button5['text'] = "O"
                    break
                elif k == 6 and button6['text'] != 'X':
                    button6['text'] = "O"
                    break
                elif k == 7 and button7['text'] != 'X':
                    button7['text'] = "O"
                    break
                elif k == 8 and button8['text'] != 'X':
                    button8['text'] = "O"
                    break
                elif k == 9 and button9['text'] != 'X':
                    button9['text'] = "O"
                    break
        bclick = True
        checkForWin()
        flag += 1
                
    else:
        messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
    global a
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
            button1.configure(bg = 'pink');button2.configure(bg = 'pink');button3.configure(bg = 'pink')
        elif(button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
            button4.configure(bg = 'pink');button5.configure(bg = 'pink');button6.configure(bg = 'pink')
        elif(button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
            button7.configure(bg = 'pink');button8.configure(bg = 'pink');button9.configure(bg = 'pink')
        elif(button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
            button3.configure(bg = 'pink');button5.configure(bg = 'pink');button7.configure(bg = 'pink')
        elif(button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
            button1.configure(bg = 'pink');button4.configure(bg = 'pink');button7.configure(bg = 'pink')
        elif(button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
            button2.configure(bg = 'pink');button5.configure(bg = 'pink');button8.configure(bg = 'pink')
        elif(button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
            button3.configure(bg = 'pink');button6.configure(bg = 'pink');button9.configure(bg = 'pink')
        elif(button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
            button1.configure(bg = 'pink');button5.configure(bg = 'pink');button9.configure(bg = 'pink')
        disableButton()
        data['played'][index_of_player] += 1
        data['win'][index_of_player] += 1
        df = pd.DataFrame(data,columns = ['name','played','win','lose','tie'])
        df.to_csv('c.csv')
        imgx = Button(frame,width = 163,height =173,image = photoimagez,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
        imgy = Button(frame,width = 163,height =173,image = photoimagey,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
        messagebox.showinfo("Tic-Tac-Toe", pa)
        a = []
        return 1

    elif(flag == 8):
        data['played'][index_of_player] += 1
        data['tie'][index_of_player] += 1
        df = pd.DataFrame(data,columns = ['name','played','win','lose','tie'])
        df.to_csv('c.csv')
        imgx = Button(frame,width = 163,height =173,image = photoimaget,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
        imgy = Button(frame,width = 163,height =173,image = photoimaget,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
        messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        a = []
        return 1
        

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'):
            button1.configure(bg = 'pink');button2.configure(bg = 'pink');button3.configure(bg = 'pink')
        elif(button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'):
            button4.configure(bg = 'pink');button5.configure(bg = 'pink');button6.configure(bg = 'pink')
        elif(button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'):
            button7.configure(bg = 'pink');button8.configure(bg = 'pink');button9.configure(bg = 'pink')
        elif(button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
            button3.configure(bg = 'pink');button5.configure(bg = 'pink');button7.configure(bg = 'pink')
        elif(button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'):
            button1.configure(bg = 'pink');button4.configure(bg = 'pink');button7.configure(bg = 'pink')
        elif(button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'):
            button2.configure(bg = 'pink');button5.configure(bg = 'pink');button8.configure(bg = 'pink')
        elif(button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
            button3.configure(bg = 'pink');button6.configure(bg = 'pink');button9.configure(bg = 'pink')
        elif(button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'):
            button1.configure(bg = 'pink');button5.configure(bg = 'pink');button9.configure(bg = 'pink')
        disableButton()
        data['played'][index_of_player] += 1
        data['lose'][index_of_player] += 1
        df = pd.DataFrame(data,columns = ['name','played','win','lose','tie'])
        df.to_csv('c.csv')
        imgx = Button(frame,width = 163,height =173,image = photoimagek,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
        imgy = Button(frame,width = 163,height =173,image = photoimagex,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
        messagebox.showinfo("Tic-Tac-Toe", playerb)
        a = []
        return 1
        

def close_it():
    tk.destroy()

def again():
    global flag,a
    button1.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button2.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button3.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button4.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button5.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button6.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button7.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button8.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    button9.configure(state=ACTIVE,text = ' ',bg = 'skyblue')
    flag = 0
    a = []
    imgx = Button(frame,width = 163,height = 173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
    imgx = Button(frame,width = 163,height = 173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
    imgy = Button(frame,width = 163,height =173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
    imgy = Button(frame,width = 163,height =173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)




buttons = StringVar()

img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 11,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 12,padx = 0)

head = Label(tk, text="PLAYER1 V/S COMPUTER", font='Times 25 bold', bg='yellow', fg='red', height=1, width=20).grid(row = 0,column = 10,columnspan = 3,pady = 0)


label = Label( tk, text="Player 1:", font='Times 25 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=10,pady = 20)


#label = Label( tk, text="Player 2:", font='Times 25 bold', bg='white', fg='black', height=1, width=8)
#label.grid(row=3, column=10)

button1 = Button(tk, text=" ", font='Times 25 bold',bg='skyblue', fg='white', height=4, width=8,command=lambda: btnClick(button1,1))
button1.grid(row=4, column=10)

button2 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button2,2))
button2.grid(row=4, column=11)

button3 = Button(tk, text=' ',font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button3,3))
button3.grid(row=4, column=12)

button4 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button4,4))
button4.grid(row=5, column=10)

button5 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button5,5))
button5.grid(row=5, column=11)

button6 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button6,6))
button6.grid(row=5, column=12)

button7 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button7,7))
button7.grid(row=6, column=10)

button8 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button8,8))
button8.grid(row=6, column=11)

button9 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', fg='white', height=4, width=8, command=lambda: btnClick(button9,9))
button9.grid(row=6, column=12)

img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 11,padx = 0)
button10 = Button(tk,text = 'PLAY AGAIN',font = 'Times 15 bold',fg = 'white',bg = 'skyblue',command = again).grid(row = 7,column = 10,pady = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 12,padx = 0)
button11 = Button(tk,text = 'EXIT',font = 'Times 15 bold',fg = 'white',bg = 'skyblue',command = close_it).grid(row = 7,column = 12,pady = 0)


img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 0,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 1,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 3,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 13,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 14,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 15,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 16,padx = 0)

img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 0,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 1,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 3,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 13,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 14,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 15,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 16,padx = 0)



img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 0,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 1,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 3,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 11,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 12,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 13,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 14,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 15,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 1,column = 16,padx = 0)


img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 0,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 1,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 3,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 13,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 14,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 15,padx = 0)
img = Label(frame,height = 75,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 16,padx = 0)


'''img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 0,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 1,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 3,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 13,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 14,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 15,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 16,padx = 0)'''


img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 0,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 1,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 3,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 13,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 14,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 15,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 4,column = 16,padx = 0)

img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 0,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 3,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 13,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 15,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 5,column = 16,padx = 0)

img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 0,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 1,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 3,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 13,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 14,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 15,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 6,column = 16,padx = 0)

img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 0,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 1,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 3,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 13,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 14,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 15,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 16,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 10,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 11,padx = 0)
img = Label(frame,height = 173,width = 163,image = photoimage,highlightthickness = 0).grid(row = 8,column = 12,padx = 0)


tk.mainloop()

