import random
from math import trunc
from random import randint
import time
import keyboard

dadJokes = []


def titleScreen():
    choice = input("How hot are flaming hot cheetos compared to peppers? Press 1 to continue")
    if choice == "1":
        quiz()

def quiz():
    cheetoAmt = 0
    thing = input("Select a  pepper:   1) Habanero    2) Ghost Pepper   3)  Carolina Reaper")
    if thing == "1":
        cheetoAmt = 100000/30000
    if thing == "2":
        cheetoAmt = 1000000/30000
    if thing == "3":
        cheetoAmt = 1641000/30000

    print("You will need to eat " + str(round(cheetoAmt, 2)) + " bags of cheetos to match that pepper")
titleScreen()
