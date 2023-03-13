import imp


import random
tries= 0
random = random.randint(1,100)
while tries <= 3 :
    value = input("enter a number between 1 and 100: ")
    if value == int(random):
        print("You Won!")
    else:
        tries += 1
        print("Welp! Try Again")
        print("Tries left: %d" % (tries))
    


