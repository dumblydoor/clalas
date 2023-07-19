#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 17:43:33 2023

@author: aquilavijayanayagam
"""

from tkinter import*
import random
from PIL import ImageTk,Image
root=Tk()
root.title("infinite dice game")
root.geometry("600x400")

root.configure(background='yellow')

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))


player1 =Label(root,text='player 1',bg='blue',fg='yellow')
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2 =Label(root,text='player 2',bg='blue',fg='yellow')
player2.place(relx=0.8,rely=0.3,anchor=CENTER)

score1 =Label(root,text='',bg='blue',fg='yellow')
score1.place(relx=0.1,rely=0.4,anchor=CENTER)

score2 =Label(root,text='',bg='blue',fg='yellow')
score2.place(relx=0.8,rely=0.4,anchor=CENTER)

random_dice=Label(root) 
random_dice.place(relx=0.5, rely=0.5,anchor=CENTER)

player1_score=0
def player1():
  global player1_score
  random_no=random.randint(1,6)
  random_dice["text"]="payer 1 dice random number : " +str(random_no)
  score1["text"] =str(player1_score)
  player1["text"]=str(player1_score)

player1_btn=Button(root, image=img, command=player_1)
player1_btn.place(relx=0.1,rely=0.6,anchor=CENTER)

def player2():
  global player2_score
  random_no=random.randint(1,6)
  random_dice["text"]="payer 1 dice random number : " +str(random_no)
  score2["text"] =str(player2_score)
  player2["text"]=str(player2_score)

player2_btn=Button(root, image=img, command=player_1)
player2_btn.place(relx=0.9,rely=0.6,anchor=CENTER)
  

root.mainloop()