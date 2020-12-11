import tkinter
from tkinter import *
import random
from tkinter import messagebox
answer =[
    ["nice frnd","bstfrnd","time pass","kux ar"],
    ["nice frnd","bstfrnd","baba","special name"],
    ["class time","Tea time","trip","kabhi nhi"],
    ["nice frnd","bstfrnd","time pass","given a sweet name"],
    ["yes ", "no","very imp","not much"],
    ["bachpan m","school time","collage time","not remenber"],
    ["nothing","nothing","nothing","nothing"],
    ["everything","everything","everything","everything",],
]
question = [
    "Who am I for You",
    "What you call me",
    "Best memory with me",
    "what I call you ",
    "Is I am important for you",
    "when we met",
    "good in me",
    "bad in me",
]
indexes = []
def gen():
    global indexes
    while(len(indexes)<5) :
        x = random.randint(0,4)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def quizstarted():
    labelnxtpage = Label(
        root,
        text = "QUIZ - Started",
        font = ("Comic sans MS","16"),
        bg="white"
    )
    labelnxtpage.pack(pady =30)
    labelfrques = Label(
        root,
        text =question[indexes[0]],
        font = ("Comic sans MS","13"),
        width = 100,
    )
    labelfrques.pack(pady=10)
    radiovar = IntVar()
    radiovar.set(0)
    radio1 = Radiobutton(
        root,
        text = answer[indexes[0]][0],
        font=("Comic sans MS","12"),
        value= 0,
        variable = radiovar,
    )
    radio1.pack(pady=4)
    radio2 = Radiobutton(
        root,
        text=answer[indexes[0]][1],
        font=("Comic sans MS", "12"),
        value=0,
        variable=radiovar,
    )
    radio2.pack(pady=4)
    radio3 = Radiobutton(
        root,
        text=answer[indexes[0]][2],
        font=("Comic sans MS", "12"),
        value=0,
        variable=radiovar,
    )
    radio3.pack(pady=4)
    radio4 = Radiobutton(
        root,
        text=answer[indexes[0]][3],
        font=("Comic sans MS", "12"),
        value=0,
        variable=radiovar,
    )
    radio4.pack(pady=4)
    sub=Button(
        root,
        text="Submit",
        font=("Cosmic sans MS","16"),
        command=""
    )
    sub.pack(pady=20)
def afterclickingstart():
    labelinstruction.destroy()
    labelquiz.destroy()
    labelimage.destroy()
    btnstart.destroy()
    gen()
    quizstarted()

root = Tk()
root.title("quiz")
root.geometry("600x600")
root.config(background ="white")
photo = PhotoImage(file = "transparentGradHat.png")
photo2 =PhotoImage(file = "Frame.png")
labelimage = Label(
    root,
    image = photo,
    bg = "white"
)
labelimage.pack(pady=(40,0))
labelquiz = Label(
    root,
    text = "Quiz-Game",
    font  = ("Comic sans MS","16"),
    bg = "white"
)
labelquiz.pack(pady=10)
btnstart = Button(
    root,
    image = photo2,
    border = 0,
    bg = "white",
    command = afterclickingstart
)
btnstart.pack(pady=30)
labelinstruction = Label(
    root,
    text = "Before start your Quiz\n please read carefully Terms & Condition",
    justify = "center",
    width ="100"
)
labelinstruction.pack()
root.mainloop()