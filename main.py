from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os 
import turtle
from vpython import *
import pygame
import webbrowser 

root=Tk()
root.title("Gates XP")
root.geometry(("800x600"))
root.config(bg="red")
url="https://www.instagram.com/graphicartifex/"
new=1
path = "C:/Users/hp/Desktop/Phython code/THEBESTSOFTWARE/wallpaper.jpg"

#defs for the button 
def clickedmycom():
    newwin = Toplevel()
    newwin.geometry("800x600")
    com = "C:/Users/hp/Desktop/Phython code/THEBESTSOFTWARE/nothing.jpg"
    mycom = Image.open(com)
    resized = mycom.resize((800,600), Image.ANTIALIAS)
    final = ImageTk.PhotoImage(resized)
    Mycomputer=tk.Label(newwin,image=final)
    Mycomputer.place(x=400,y=300,anchor="center")
    OPTIONS = ["New", "Open", "Create", "Exit"]
    variable = StringVar(newwin)
    variable.set(OPTIONS[0]) # default value

    w = OptionMenu(newwin, variable, *OPTIONS)
    w.place(x=50,y=10,anchor="center")
    newwin.mainloop()

def clickedonrec():
    newwin = Toplevel()
    newwin.geometry("800x600")
    com = "C:/Users/hp/Desktop/Phython code/THEBESTSOFTWARE/spong.jpg"
    mycom = Image.open(com)
    resized = mycom.resize((800,600), Image.ANTIALIAS)
    final = ImageTk.PhotoImage(resized)
    Mycomputer=tk.Label(newwin,image=final)
    Mycomputer.place(x=400,y=300,anchor="center")
    
    label.pack()
    newwin.mainloop()

def clickedonturtle():
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)

def clickedon3d():
    sphere(pos=vector(0,0,0),radias=1,color=color.red)

def openweb():
    webbrowser.open(url,new=new)


def clickedonplaygame():
    pygame.init()     
    win = pygame.display.set_mode((500, 500))     
    x = 200
    y = 200   
    width = 20
    height = 20    
    vel = 3    
    run = True
    while run:   
        pygame.time.delay(10)    
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:   
                run = False
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and x>0: 
            x -= vel 
        if keys[pygame.K_RIGHT] and x<500-width: 
            x += vel 
        if keys[pygame.K_UP] and y>0: 
            y -= vel 
        if keys[pygame.K_DOWN] and y<500-height:  
            y += vel 
        if keys[pygame.K_SPACE]:
            y-=10
        win.fill((0, 0, 0)) 
        objone = pygame.draw.rect(win, (225, 225, 0), (x, y, width, height))  
        pygame.display.update()  
    pygame.quit() 

#img for the wallpaper
my_pic = Image.open(path)
resized_pic = my_pic.resize((800,600) , Image.ANTIALIAS)
finalpic = ImageTk.PhotoImage(resized_pic)
label=tk.Label(root, image=finalpic)
label.pack()

#img for the my computer icon
com = "C:/Users/hp/Desktop/Phython code/THEBESTSOFTWARE/images.jpg"
mycom = Image.open(com)
resized = mycom.resize((50,50), Image.ANTIALIAS)
final = ImageTk.PhotoImage(resized)
Mycomputer=tk.Label(root,image=final)
Mycomputer.place(x=50,y=30,anchor="center")

#img for square graphics icon
com = "C:/Users/hp/Desktop/Phython code/THEBESTSOFTWARE/square.jpg"
squr = Image.open(com)
resizedsqur = squr.resize((50,50), Image.ANTIALIAS)
squrfinal = ImageTk.PhotoImage(resizedsqur)
squaregraphicsimg=tk.Label(root,image=squrfinal)
squaregraphicsimg.place(x=400,y=250,anchor="center")

#img for the my recycle bin icon
com = "C:/Users/hp/Desktop/Phython code/THEBESTSOFTWARE/recyclebin.png"
recyclebin = Image.open(com)
recyclebinresize = recyclebin.resize((50,50), Image.ANTIALIAS)
recyclebinfinal = ImageTk.PhotoImage(recyclebinresize)
recyclebinlable=tk.Label(root,image=recyclebinfinal)
recyclebinlable.place(x=50,y=150,anchor="center")

#button for my computer
mycombut = tk.Button(root, text="My computer", bg="white", fg="black", command=clickedmycom)
mycombut.place(x=50,y=90,anchor="center")

#button for my recycle
recyclebinbut = tk.Button(root, text="Recycle bin", bg="white", fg="black", command=clickedonrec)
recyclebinbut.place(x=50,y=200,anchor="center")

#button for draw graphics
drwagraphicsbutn = tk.Button(root, text="Draw Square graphics", bg="white", fg="black", command=clickedonturtle)
drwagraphicsbutn.place(x=400,y=300,anchor="center")

#button for draw3d graphics
clickedon3dbutton = tk.Button(root, text="Make a 3d sphere", bg="white", fg="black", command=clickedon3d)
clickedon3dbutton.place(x=400,y=200,anchor="center")

#button for playing a boring game
boringgamebutn = tk.Button(root, text="Play a boring game", bg="white", fg="black", command=clickedonplaygame)
boringgamebutn.place(x=400,y=500,anchor="center")

#button for opening my instagram
followmeoninsta = tk.Button(root, text="follow me on insta CLICK ME !", bg="white", fg="black", command=openweb)
followmeoninsta.place(x=400,y=550,anchor="center")


root.mainloop()