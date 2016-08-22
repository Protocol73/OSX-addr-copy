#Test_button.py
#the imports
import sys
import Tkinter 
import subprocess
from Tkinter import *
#This is what gets copy into the clipboard
BT1 = "Edit this"
BT2 = "Edit this"
BT3 = "Edit this"
BT4 = "Edit this"
BT5 = "Edit this"
BT6 = "Edit this"
BT7 = "Edit this"
BT8 = "Edit this"

#The Definions 
def cbp(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))    
def bt1():
    bt1 = cbp(BT1)
def bt2():
    bt2 = cbp(BT2)
def bt3():
    bt3 = cbp(BT3)    
def bt4():
    bt4 = cbp(BT4)
def bt5():
    bt5 = cbp(BT5)
def bt6():
    bt6 = cbp(BT7)
def bt7():
    bt7 = cbp(BT6)        
def bt8():
    bt8 = cbp(BT8)
def clear():
    clear = cbp("") 
def end():
    end = exit()    
def test():
    print("This Works") #for later use 
#--- The Window ---
gui = Tk()
gui.geometry("225x300")
gui.title("My Addresses")
Atext = Label(gui,text=" Press to Copy Text to Clipboard") 
Atext.pack()
# --- The Menu --- for later use
menu = Menu(gui)
gui.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Edit Varibales" , menu=subMenu)
subMenu.add_command(label="Test" ,command=test)
subMenu.add_separator()
subMenu.add_command(label="Exit" ,command=gui.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Other" , menu=editMenu)
editMenu.add_command(label="Test" ,command=test)
editMenu.add_command(label="Test" ,command=test)
#--- The Buttons ---
b1 = Button(text = "Button text",command = BT1).pack()
b2 = Button(text = "Button text",command = BT2).pack()
b3 = Button(text = "Button text",command = BT3).pack()
b4 = Button(text = "Button text",command = BT4).pack()
b5 = Button(text = "Button text",command = BT5).pack()
b6 = Button(text = "Button text",command = BT6).pack()
b7 = Button(text = "Button text",command = BT7).pack()
b8 = Button(text = "Button text",command = BT8).pack()
b9 = Button(text = "Clear Clipboard",command = clear).pack()
b10 = Button(text = "Exit",command = end).pack()
#end Program
gui.configure()
#the loop
gui.mainloop()
