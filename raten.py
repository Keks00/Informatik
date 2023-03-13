import random
tries = 0
int1 = 1
tries2= int(input("How many times do you want to try?: "))
while  type(tries2) != type(int1):
    tries2= input("How many times do you want to try?(only numbers): ")
to = int(input("To what range do you want to go?: "))
while not type(to) == type(int1):
    to = int(input("To what range do you want to go? (only numbers):"))
random = random.randint(1,(int(to)))
while tries <= (int(tries2)) :
    value = int(input("enter a number between 1 and %d: " % (int(to))))
    if value == random:
        print("You Won!")
        tries =+ int(tries2)
    elif int(tries) < int(tries2) - 1:
        tries += 1
        print("Welp! Try Again")
        if value > random:
            print("Too High!")
        else:
            print("Too Low!")
            print("Tries left: %d" % (int(tries2) - int(tries)))
    else:
        print("You Lost!")
        tries =+ tries2