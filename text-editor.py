import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def close():
    exit()
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
def cut():
    copy()
    text.delete("sel.first","sel.last")
def paste():
    text.insert(INSERT,text.clipboard_get())
def new():
    text.delete(1.0,END)
def openn():
    filedialog.askopenfile(initialdir="Desktop",title="select file")
    text.insert(END , line)

def savee():
    f =filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if f is None:
        return
    text2save = text.get(1.0 , END)
    f.write(text2save)
    f.close()

root =Tk()

root.geometry("500x500")
main_menu =Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="File" , menu =file_menu)
Edit_menu = Menu(main_menu)
main_menu.add_cascade(label ="Edit",menu=Edit_menu)
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open", command=openn)
file_menu.add_command(label="Save",command=savee)
file_menu.add_command(label = "Exit",command = close)
Save = Menu(file_menu)
Save.add_command(label="Save As New",command =savee)
Edit_menu.add_command(label="Copy",command=copy)
Edit_menu.add_command(label="Cut",command=cut)
Edit_menu.add_command(label="Paste",command=paste)
font_menu=Menu(main_menu)
main_menu.add_cascade(label="Font",menu=font_menu)
settin_menu=Menu(main_menu)
main_menu.add_cascade(label ="Setting",menu =settin_menu)
text = Text(
    root,
)
text.pack(fill= BOTH ,expand =Y)
root.title("Text-Editor")
root.resizable(0,0)
root.mainloop()