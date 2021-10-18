import random
num = random.randint(0,20)
player = input("guess: ")
while True:
    if player == str(num):
        print("Win!")
        break
    elif str(player) == "help":
        if num > 10:
            print("its bigger then 10")
        elif num < 10:
            print("its samller then 10")
        else:
            print("its not bigger or smaller than 10 so ...")
    player = input("guess again: ")
