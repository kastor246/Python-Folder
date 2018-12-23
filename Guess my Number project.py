#Guess the number

import random
import sys


Finished = 0
while Finished != "Done":
    User = input("Enter a number! 1-50 ")
    try:
        User = int(User)
        break
    except ValueError:
        print("Try again!")


if Finished == 0:
    f = random.randint(1, 50)
    if User > f:
        print("Too High!")
    if User < f:
        print("Too low!")


def UserInput(self, UserInput):
    self.UserInput = while Finished != "Done":
        
        User = input("Enter a number! 1-50 ")
        try:
            User = int(User)
            break
        except ValueError:
            print("Try again!")
    
    
