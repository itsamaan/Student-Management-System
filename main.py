from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Amaan' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        
    else:
        messagebox.showerror('Error','Please enter correct credentials')



window=Tk()

window.geometry('1280x700+0+0')

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')





window.mainloop()



Still in progress.........
