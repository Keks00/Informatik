import time
import random
difficulty = 1
difficulty_text = "easy"
with open('player/saved/stats.json') as balance:
    money = int(balance.read())
selection = "1"
menu = True
while menu == True:
    if difficulty == 1:
        difficulty_text = "easy"
    if difficulty == 2:
        difficulty_text = "medium"
    if difficulty == 3:
        difficulty_text = "hard"
    if difficulty == 4:
        difficulty_text = "dangerous"
    if difficulty == 5:
        difficulty_text = "impossible"
    else:
        difficulty_text = "invalid"
        difficulty = 0
    print("_Menu_")
    time.sleep(0.4)
    print("1. Select difficulty. Current : %s " % (difficulty_text))
    time.sleep(0.2) 
    print("2. Select shop. Your balance : %s" % (money))
    time.sleep(0.2)
    print("3. Select Level")
    selection = input("Select your action: ")
    if selection == "1":
        difficulty = int(input("Select the difficulty: "))    
    if selection == "2":
        print("the Shop is unavailible")
    if selection == "3":
        print()
