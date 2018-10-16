#Github https://github.com/Protocol73/OSX-addr-copy
#only works on osx see Github for modding for Windows use.

#the imports
import os
import sys
import tkinter
import subprocess
import configparser
from tkinter import *
from tkinter import messagebox

#Read Config File
cfg_file = configparser.ConfigParser()   
configFilePath = r'clipboardButtons.cfg'
cfg_file.read(configFilePath)

#This is what gets copy into the clipboard

CB_txt1 = cfg_file.get('ButtonClipboardText', 'Button1')
CB_txt2 = cfg_file.get('ButtonClipboardText', 'Button2')
CB_txt3 = cfg_file.get('ButtonClipboardText', 'Button3')
CB_txt4 = cfg_file.get('ButtonClipboardText', 'Button4')
CB_txt5 = cfg_file.get('ButtonClipboardText', 'Button5')
CB_txt6 = cfg_file.get('ButtonClipboardText', 'Button6')
CB_txt7 = cfg_file.get('ButtonClipboardText', 'Button7')
CB_txt8 = cfg_file.get('ButtonClipboardText', 'Button8')

BT_display_txt1 = cfg_file.get('ButtonDisplayText', 'Button1')
BT_display_txt2 = cfg_file.get('ButtonDisplayText', 'Button2')
BT_display_txt3 = cfg_file.get('ButtonDisplayText', 'Button3')
BT_display_txt4 = cfg_file.get('ButtonDisplayText', 'Button4')
BT_display_txt5 = cfg_file.get('ButtonDisplayText', 'Button5')
BT_display_txt6 = cfg_file.get('ButtonDisplayText', 'Button6')
BT_display_txt7 = cfg_file.get('ButtonDisplayText', 'Button7')
BT_display_txt8 = cfg_file.get('ButtonDisplayText', 'Button8')



#The Definions 
def copyToClipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))    
def bt1():
    bt1 = copyToClipboard(CB_txt1)
def bt2():
    bt2 = copyToClipboard(CB_txt2)
def bt3():
    bt3 = copyToClipboard(CB_txt3)    
def bt4():
    bt4 = copyToClipboard(CB_txt4)
def bt5():
    bt5 = copyToClipboard(CB_txt5)
def bt6():
    bt6 = copyToClipboard(CB_txt7)
def bt7():
    bt7 = copyToClipboard(CB_txt6)        
def bt8():
    bt8 = copyToClipboard(CB_txt8)
def clear():
    clear = copyToClipboard("") 
def end():
    end = exit()    
def test():
    messagebox.showwarning('Notice',"This doesn't do anything yet.") #for later use 
def reload():
    os.execl(sys.executable, sys.executable, *sys.argv)

#--- The Window ---
gui = Tk()
gui.title("Clipboard Buttons")
Windowtext = Label(gui,text=" Press to Copy Text to Clipboard") 
Windowtext.pack()

# --- The Menu --- for later use
menu = Menu(gui)
gui.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Edit Varibales" , menu=subMenu)
subMenu.add_command(label="8 of These" ,command=test)
subMenu.add_separator()
subMenu.add_command(label="Exit" ,command=gui.quit)
subMenu.add_command(label="Restart" , command=reload)

editMenu = Menu(menu)
menu.add_cascade(label="Other" , menu=editMenu)
editMenu.add_command(label="Nothin Here" ,command=test)
#--- The Buttons ---
#Edit The cfg file to whatever you what your buttons to say

b1 = Button(text = BT_display_txt1 ,command = bt1).pack()
b2 = Button(text = BT_display_txt2 ,command = bt2).pack()
b3 = Button(text = BT_display_txt3 ,command = bt3).pack()
b4 = Button(text = BT_display_txt4 ,command = bt4).pack()
b5 = Button(text = BT_display_txt5 ,command = bt5).pack()
b6 = Button(text = BT_display_txt6 ,command = bt6).pack()
b7 = Button(text = BT_display_txt7 ,command = bt7).pack()
b8 = Button(text = BT_display_txt8 ,command = bt8).pack()
b9 = Button(text = "Clear Clipboard",command = clear).pack()
#end Program
gui.configure()
#the loop
gui.mainloop()
