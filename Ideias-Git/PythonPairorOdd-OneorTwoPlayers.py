from imp import reload
import time
import math
from unittest import result

print('Hey, welcome to pair and odd program gaming')
time.sleep(1)
print('Developed by NEVESGF v1.2')
time.sleep(1)
print('----')
print(' -- ')
print('----')
time.sleep(1)
while True:
    qty_players = int(input("Enter quantity of players ONE or TWO = (NUMBERS ONLY) "))
    if qty_players == 1 or qty_players == 2:
        print("...Loading...")
        time.sleep(1)
        break
    else:
        print("This quantity of players is not avaiable !")
        print("Restarting the program")
        time.sleep(1)
        continue

if qty_players == 1:
        nameofplayer = input("What's your name? ")
        while True:
            choiseofplayer = input(nameofplayer + " do you want pair or odd = ")
            if choiseofplayer == "pair" or choiseofplayer == "odd":
                import random
                from sqlite3 import paramstyle
                randomnumber = random.randint(0,50)
                print(randomnumber)
                if (randomnumber % 2) == 0:
                    randomnumberresult = "pair"
                else:
                    randomnumberresult = "odd"
                if choiseofplayer == randomnumberresult :
                    print("CONGRATULATIONS YOU WIN")
                    restartgame = input("Do you wanna try again ? (Y/N)")
                    if restartgame == 'Y':
                        continue
                    else:
                        break
                else:
                    print("You LOST, try again")
                    restartgame = input("Do you wanna try again ? (Y/N)")
                    if restartgame == 'Y':
                        
                        continue
                    else:
                        break
            else:
                print("This is not acceptable, try again")
                time.sleep(1)
                continue
exit

if qty_players ==2:
    while True:
        playerone = input("Insert the name of first player = ")
        playertwo = input("Insert the name of second player = ")
        playeronechoice = input(playerone + ' Do you want pair or odd? ')
        playertwochoice = input(playertwo + ' Do you want pair or odd? ')
        if playeronechoice == playertwochoice:
            print("You can't not choose the same thing, try again")
            continue
        else:
            print("It's time to choose your numbers")
            playeronenumber = int(input(playerone + " choose a number = "))
            playertwonumber = int(input(playertwo + " choose a number = "))
            break
    resultnumber = playeronenumber + playertwonumber
    if (resultnumber % 2) == 0:
        resultchoise = "pair"
    else:
        resultchoise = "odd"
    if resultchoise == playeronechoice:
        print(playerone + " YOU WIN !!!")
    else:
        print(playertwo + " YOU WIN !!!")
exit
