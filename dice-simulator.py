#import the required libraries
#packages required: tkinter & random
import random
from tkinter import *

root = Tk() #create tkinter(GUI) instance
root.title("Dice_Roller")

root.geometry("800x400") #define the height and width of the GUI

#components required in GUI 1. button - rolling of dice 2. label 

l1 = Label(root, font = ("times", 200)) #font and size of the text on button

#create dice list
def roll():  #define the function roll
	number = ['\u2680', '\u2681', '\u2683', '\u2684', '\u2685'] #list of ask key character of the string stored in number
	l1.config(text = f'{random.choice(number)}{random.choice(number)}') #text formatting - roll random dice
	l1.pack() 

#create roll button
button_1 = Button(root,text = " let's roll the dice! ", width = 20, command = roll) #GUI instance, text on the button, command that button triggers

button_1.place(x = 340 , y = 0) #position of the button

roll()

root.mainloop() #close the mainloop
