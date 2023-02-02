from tkinter import *
import winsound
root = Tk()
root.config(background='#67e0cc')
root.geometry("600x300")
root.resizable(0,0)
def viewOptions():
    winsound.MessageBeep()
    t.forget()
    def closeBox():
        dialogBox.forget()
        btn_show.pack()
        t.pack()
    def playGame():
        dialogBox.forget()
        Label(root,text="You are playing a good game",font=15,bg='#67e0cc').pack()
    btn_show.forget()
    dialogBox = Frame(root,height=130,width=400,borderwidth=5,relief="raised",bg="#f58e97")
    play_btn=Button(dialogBox,text="Play",font=("Bebas Neue",17),width=15,bg="#75b4d9",fg="#ffffff",command=playGame)
    close_btn=Button(dialogBox,text="Close",font=("Bebas Neue",17),width=15,bg="#348a47",fg="#ffffff",command=closeBox)
    play_btn.grid(row=0,column=0,padx=20,pady=20)
    close_btn.grid(row=0,column=1,padx=20,pady=20)
    dialogBox.grid_propagate(False)
    dialogBox.pack(padx=100,pady=100)
btn_show = Button(root,text="Play game!",font=("Koulen",15),command=viewOptions)
btn_show.pack()
t=Label(root,text="you are going to play a very good game!!!",font=15,bg='#67e0cc')
t.pack()
root.mainloop()
