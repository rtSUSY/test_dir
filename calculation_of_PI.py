# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:37:18 2018
@author: rtSUSY
"""
import random
import math
import time

def calcpi():
    NUM = input("Type a number to loop the code: ")
    NUM = int(NUM)

#    answ = input("It costs so long time, Okay?(y/n):")
#    NUM = sys.maxsize
#    print("NUM is {}".format(NUM))
    
    num_in_circle = 0
    num_out_circle = 0
    for i in range(0, NUM):
#        if answ=="y":
#            pass
#        elif answ=="n":
#            break
#        else:  
#            raise ValueError("ERROR:YOU MUST TYPE y or n!!!")
    
        x_random = random.random()
        y_random = random.random()
        radius_circle = math.sqrt(x_random**2 + y_random**2)
        
        if radius_circle <= 1:
            num_in_circle  += 1
        else:
            num_out_circle += 1
    
    pi_ = 4*(num_in_circle/NUM)
    #print("Pi is calculated as ", pi_)
    #print(NUM, ":", num_in_circle + num_out_circle)
    
    return pi_
    
    
### Main ###
if __name__=="__main__":
    start = time.time()
    print("Pi is calculated as ", calcpi())
    end   = time.time()
    running_time = end - start
    print(running_time)