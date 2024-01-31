from tkinter import*
from PIL import ImageTk,Image
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("White board")
root.geometry("1100x600")
root.iconbitmap("./img.ico")

stroke_size = IntVar()
stroke_size.set(1)

strokecolor = StringVar()
strokecolor.set("black")

#frame 1 - Tools

frame1 = LabelFrame(root,height=100,width=1100)
frame1.grid(row=0,column=0,sticky=NW)

#toolsframe

toolsframe = Frame(frame1,height=100,width=100,bg="green",relief=SUNKEN,borderwidth=3)
toolsframe.grid(row=0,column=0)

#variable for pencil

def usepencil():
    strokecolor.set("black")
    canvas["cursor"] = "arrow"

def useeraser():
    strokecolor.set("white")
    canvas["cursor"] = DOTBOX

pencil = PhotoImage(file="./img2.png")
Button(toolsframe,image=pencil, command=usepencil).grid(row=0,column=0)

eraser = PhotoImage(file="./img.png")
Button(toolsframe,image=eraser, command=useeraser).grid(row=1,column=0)

#sizeframe

sizeframe = Frame(frame1,height=100,width=100,bg="green",relief=SUNKEN,borderwidth=3)
sizeframe.grid(row=0,column=1)

options = [1,2,3,4,5,10]
 
size_list = OptionMenu(sizeframe,stroke_size,*options)
size_list.grid(row=1,column=0)


#colorboxframe

colorboxframe = Frame(frame1,height=100,width=100,bg="green",relief=SUNKEN,borderwidth=3)
colorboxframe.grid(row=0,column=2)

def selectcolor():
    selectedcolor = colorchooser.askcolor(title="Select color")
    if selectedcolor[1] == None:
        strokecolor.set("black")
    else:
        strokecolor.set(selectedcolor[1])
  

colorboxbutton = PhotoImage(file="./img3.png")
Button(colorboxframe,image=colorboxbutton,command=selectcolor).grid(row=0,column=0)

#colorsframe

colorsframe = Frame(frame1,height=100,width=100,bg="green",relief=SUNKEN,borderwidth=3)
colorsframe.grid(row=0,column=3)

black = Button(colorsframe,bg="black",width=2,height=1,command=lambda:strokecolor.set("black"))
black.grid(row=0,column=0)

red = Button(colorsframe,bg="red",width=2,height=1,command=lambda:strokecolor.set("red"))
red.grid(row=1,column=0)

orange = Button(colorsframe,bg="orange",width=2,height=1,command=lambda:strokecolor.set("orange"))
orange.grid(row=0,column=1)

yellow = Button(colorsframe,bg="yellow",width=2,height=1,command=lambda:strokecolor.set("yellow"))
yellow.grid(row=1,column=1)

blue = Button(colorsframe,bg="blue",width=2,height=1,command=lambda:strokecolor.set("blue"))
blue.grid(row=0,column=2)

green = Button(colorsframe,bg="green",width=2,height=1,command=lambda:strokecolor.set("green"))
green.grid(row=1,column=2)

purple = Button(colorsframe,bg="purple",width=2,height=1,command=lambda:strokecolor.set("purple"))
purple.grid(row=0,column=3)

pink = Button(colorsframe,bg="pink",width=2,height=1,command=lambda:strokecolor.set("pink"))
pink.grid(row=1,column=3)

#SaveImage Frame

def saveimage():
    fileLocation = filedialog.asksaveasfilename(defaultextension = "jpg")
    x = root.winfo_rootx()
    y = root.winfo_rooty()+100
    img = ImageGrab.grab(bbox=(x,y,x+1100,y+500))
    img.save(fileLocation)
    showimage = messagebox.askyesno("paint app","Do you want to open image?")
    if showimage:
        img.show()

def clear():
    if messagebox.askokcancel("paint app","Do you want to clear everything?"):
        canvas.delete('all')

def createnew():
    if messagebox.askyesno("paint app","Do you want to save your work?"):
        saveimage()
    clear()

saveimageframe = Frame(frame1,height=100,width=100,bg="green",relief=SUNKEN,borderwidth=3)
saveimageframe.grid(row=0,column=4)

saveimagebutton = Button(saveimageframe,bg="white",width=10,text="save",command=saveimage)
saveimagebutton.grid(row=0,column=0)

newimagebutton = Button(saveimageframe,bg="white",width=10,text="New",command=createnew)
newimagebutton.grid(row=1,column=0)

clearimagebutton = Button(saveimageframe,bg="white",width=10,text="Clear",command=clear)
clearimagebutton.grid(row=2,column=0)

#settingframe    

def help():
  messagebox.showinfo("Help","1. Click on the color circle to select customized color\n2. Click on clear to clear the whole page\n3. Right click for dotted lines\n4. Press the cursor button to place the text from textbox")

def setting():
    messagebox.showwarning("Setting","Not Available")

def about():
    messagebox.showinfo("About","The paint app is the best!")


settingframe = Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
settingframe.grid(row=0,column=5)

helpbutton = Button(settingframe,bg="white",width=10,text="Help",command=help)
helpbutton.grid(row=0,column=0)

settingbutton = Button(settingframe,bg="white",width=10,text="Setting",command=setting)
settingbutton.grid(row=1,column=0)

aboutbutton = Button(settingframe,bg="white",width=10,text="About",command=about)
aboutbutton.grid(row=2,column=0)

#textframe

textvalue = StringVar()

def writetext(event):
    canvas.create_text(event.x,event.y,text = textvalue.get())

textframe = Frame(frame1,height=100,width=200,relief=SUNKEN,borderwidth=3)
textframe.grid(row=0,column=6)

texttitlebutton = Label(textframe,bg="white",width=20,text="Write your Text here")
texttitlebutton.grid(row=0,column=0)

entrybutton = Entry(textframe,textvariable=textvalue,bg="white",width=20)
entrybutton.grid(row=1,column=0)

clearbutton = Button(textframe,bg="white",width=20,text="Clear",command=lambda:textvalue.set(""))
clearbutton.grid(row=2,column=0)

#noteframe

noteframe = Frame(frame1,height=100,width=200,relief=SUNKEN,borderwidth=3)
noteframe.grid(row=0,column=7)

texttitlebutton = Text(noteframe,bg="white",width=60,height=4)
texttitlebutton.grid(row=0,column=0)


#Frame 2 - canavs

frame2 = LabelFrame(root,height=500,width=1100,bg="yellow")
frame2.grid(row=1,column=0)

canvas = Canvas(frame2,height=500,width=1100,bg="white")
canvas.grid(row=0,column=0)

#variable for pencil

prevpoint = [0,0]
currentpoint = [0,0]

def paint(event):
    global prevpoint
    global currentpoint
    x = event.x
    y = event.y
    currentpoint = [x,y]
    

    if prevpoint != [0,0]:
        canvas.create_polygon(prevpoint[0],prevpoint[1],currentpoint[0],currentpoint[1],fill=strokecolor.get(),outline=strokecolor.get(),width=stroke_size.get())
    prevpoint = currentpoint

    if event.type == "5":
        prevpoint = [0,0]

def paintright(event):
    x = event.x
    y = event.y
    canvas.create_arc(x,y,x+stroke_size.get(),y+stroke_size.get(),fill=strokecolor.get(),outline=strokecolor.get(),width=stroke_size.get())


canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
canvas.bind("<B3-Motion>",paintright)
canvas.bind("<Button-2>",writetext)





root.resizable(False,False)
root.mainloop()