import tkinter
from tkinter import filedialog
import pygame
from pygame import mixer

root =tkinter.Tk()
mixer.init()
root.title("music")
root.config(bg ="black")
root.geometry("500x400")
photo = tkinter.PhotoImage(file ="Frame.png")
global f
def play_music():
    mixer.music.load(f)
    mixer.music.play()
def pause_music():
    pygame.mixer.music.stop()
def add_music():
    global f
    global file_name
    file_name= filedialog.askopenfile()
    f=file_name
    index = 0
    liis.insert(index,f)
    index +=1
    addbtn.pack()

right = tkinter.Frame(root)
right.pack(side="left")
btn1 = tkinter.Button(
    right,
    image = photo,
    command = play_music
)
btn1.pack()
btn2 = tkinter.Button(
    right,
    text = "Stop",
    width = 9,
    height=5,
    font = ("Comic sns MS",20),
    border=0,
    command = pause_music

)
btn2.pack()
left = tkinter.Frame(root)
left.pack(pady= 30,side="right")
liis = tkinter.Listbox(
    left
)
liis.pack(side="right")
addbtn= tkinter.Button(
    left,
    text = "Add",
    height=1,
    width=5,
    command = add_music
)
addbtn.pack(side="right")

root.mainloop()