from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")
tk.configure(background = '#0789fb')

frame = Frame(tk).grid()

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()


photo = PhotoImage(file = "killit.png")
photoimage = photo.subsample(1,1)

photox = PhotoImage(file = "smile.png")
photoimagex = photox.subsample(1,1)

photoy = PhotoImage(file = "sad.png")
photoimagey = photoy.subsample(1,1)

photot = PhotoImage(file = "tie.png")
photoimaget = photot.subsample(1,1)

img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 11,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 12,padx = 0)

img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 11,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 12,padx = 0)


#variables to take the usernames from Entry widgets
player1_name = Entry(tk, textvariable=p1)
player1_name.grid(row=2, column=6, columnspan=8)
player2_name = Entry(tk, textvariable=p2)
player2_name.grid(row=3, column=6, columnspan=8)

#bclick is used to confirm the chance of player1 or player2
bclick = True
flag = 0

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



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
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
        imgx = Button(frame,width = 163,height =173,image = photoimagex,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
        imgy = Button(frame,width = 163,height =173,image = photoimagey,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        imgx = Button(frame,width = 163,height =173,image = photoimaget,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
        imgy = Button(frame,width = 163,height =173,image = photoimaget,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        
        

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
        imgx = Button(frame,width = 163,height =173,image = photoimagex,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
        imgy = Button(frame,width = 163,height =173,image = photoimagey,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

def again():
    global flag,bclick
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
    bclick = True
    imgx = Button(frame,width = 163,height = 173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
    imgx = Button(frame,width = 163,height = 173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)
    imgy = Button(frame,width = 163,height =173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 1,padx = 0)
    imgy = Button(frame,width = 163,height =173,image = photoimage,highlightthickness = 0).grid(row = 5,column = 14,padx = 0)

def close_it():
    tk.destroy()


        


buttons = StringVar()

img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 11,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 0,column = 12,padx = 0)
head = Label(tk, text="PLAYER1 V/S PLAYER2", font='Times 25 bold', bg='yellow', fg='red', height=1, width=20).grid(row = 0,column = 10,columnspan = 3,pady = 0)



label = Label( tk, text="Player 1:",font='Times 25 bold', bg='pink', fg='blue', height=1, width=8)
label.grid(row=2, column=10)


label = Label( tk, text="Player 2:", font='Times 25 bold', bg='pink', fg='blue', height=1, width=8)
label.grid(row=3, column=10,pady = 10)

button1 = Button(tk, text=" ", font='Times 25 bold', bg='skyblue',bd = 3,fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=4, column=10)

button2 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=4, column=11)

button3 = Button(tk, text=' ',font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=4, column=12)

button4 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=5, column=10)

button5 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=5, column=11)

button6 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=5, column=12)

button7 = Button(tk,text = ' ', font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=6, column=10)


button8 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue', bd = 3,fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=6, column=11)

button9 = Button(tk, text=' ', font='Times 25 bold', bg='skyblue',bd = 3, fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=6, column=12)


img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 10,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 11,padx = 0)
button10 = Button(tk,text = 'PLAY AGAIN',font = 'Times 15 bold',bd = 3,fg = 'white',bg = 'skyblue',command = again).grid(row = 7,column = 10,pady = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 7,column = 12,padx = 0)
button11 = Button(tk,text = 'EXIT',font = 'Times 15 bold',bd = 3,fg = 'white',bg = 'skyblue',command = close_it).grid(row = 7,column = 12,pady = 0)




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


img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 0,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 1,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 3,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 13,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 14,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 15,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 2,column = 16,padx = 0)


img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 0,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 1,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 3,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 13,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 14,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 15,padx = 0)
img = Label(frame,height = 50,width = 163,image = photoimage,highlightthickness = 0).grid(row = 3,column = 16,padx = 0)


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

