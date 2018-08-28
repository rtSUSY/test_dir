# -*- coding: utf-8 -*-
"""
Janken program
0: Lock
1: Paper
2: Scissors
Created on Wed Aug 22 10:24:43 2018
@author: rtSUSY
"""
import random
import time

def jajanken():
    you = int(10)
    me  = int(10)

    while (you == me):        
        you = random.randint(0,2)
        me  = random.randint(0,2)
            
        if you == me:
            print("AGAIN!!you", your_choice(you), " VS ", my_choice(me), "me")
        elif you*me != 0:
            if you > me:
                print("YOU win!!you", your_choice(you), " VS ", my_choice(me), "me")
            else:
                print(" I  win!!you", your_choice(you), " VS ", my_choice(me), "me")
        elif you*me == 0:
            if(you==1):
                print("YOU win!!you", your_choice(you), " VS ", my_choice(me), "me")
            elif(me==1):
                print(" I  win!!you", your_choice(you), " VS ", my_choice(me), "me")
            elif(you==2):
                print(" I  win!!you", your_choice(you), " VS ", my_choice(me), "me")
            elif(me==2):
                print("You win!!you", your_choice(you), " VS ", my_choice(me), "me")


def your_choice(num):
    if num == 0:
        choice = "Lock"
    elif num == 1:
        choice = "Paper"
    elif num == 2:
        choice = "Scissors"
    
    return choice


def my_choice(num):
    if num == 0:
        choice = "Lock"
    elif num == 1:
        choice = "Paper"
    elif num == 2:
        choice = "SCissors"

    return choice



### Main ###
if __name__=="__main__":
    while(True):
        jajanken()
        print("")
        time.sleep(2.5)


            
