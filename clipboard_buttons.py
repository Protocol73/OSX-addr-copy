#Written by Protocol73 - Donate BTC - 1KATaqx5F4HbsHiM3SNxWX1uAD56Cwuo8B
#the imports           - Donate ZET - ZLfctkfnsH1fxX1WxCL5UiS2U54jKeFH63
import subprocess
from Tkinter import *
#Defined Here
def cbp(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))    
# Edit what gets copyed
def Button1():
    Button1 = cbp("Edit this")
def Button2():
    Button2 = cbp("Edit this")
def Button3():
    Button3 = cbp("Edit this")    
def Button4():
    Button4 = cbp("Edit this")
def Button5():
    Button5 = cbp("Edit this") 
def Button6():
    Button6 = cbp("Edit this")       
def clear():
    clear = cbp("") 
def end():
    end = exit()     
#the window
gui = Tk()
gui.geometry("225x300")
gui.title("My Addresses")
CPtext = Label(gui,text=" Press to copy Address to Clipboard") 
CPtext.pack()          #  | 
#Copy lines;number and >  |  add def to add more buttons 
#Edit Button text There > v
b1 = Button(text = "Button-1",command = Button1).pack()
b2 = Button(text = "Button-2",command = Button2).pack()
b3 = Button(text = "Button-3",command = Button3).pack()
b4 = Button(text = "Button-4",command = Button4).pack()
b5 = Button(text = "Button-5",command = Button5).pack()
b6 = Button(text = "Button-6",command = Button6).pack()
bc = Button(text = "Clear Clipboard",command = clear).pack()
be = Button(text = "Exit",command = end).pack()
#the loop
gui.mainloop()
#The End
 

