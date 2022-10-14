import time
import random
import randomEncounters
#health = 100
#inventory
#attack damage
#spells



#randomEncounters.printAthing()

print("Hello and welcome to Mystic Bloom.")
time.sleep(2)
print("Your adventure will begin shortly.")
time.sleep(2)
print("But first we will need to find out what kind of adventurer you are!")
time.sleep(3)
print("Let's start with something easy. what's your name?")
time.sleep(2)
name = input("Enter your name... >")
time.sleep(2)
print("Ok, so your name is " + name)
time.sleep(2)
print("...you dont sound very experienced, but I guess you'll have to do")
time.sleep(2)
print(f"Well {name} you look like you got a bit of adventureing to do! let's see who you are!")
time.sleep(3)
print("Before your stands three statues.")
time.sleep(2)
print("One of a flower(1),\none of a sword(2),\nand one a piglet(3).")
startingPick1 = input("Enter 1, 2, or 3... >")
if startingPick1 == "1":
    startingPick1 = "a flower"
    print(f"{startingPick1}, good choice")
elif startingPick1 == "2":
    startingPick1 = "a sword"
    print(f"{startingPick1}, good choice") 
elif startingPick1 == "3":
    startingPick1 = "a piglet"
    print(f"{startingPick1}, good choice")
else:
    print(f"pick a number {name}, you idiot! oh well too late... ")
    startingPick1 = "no no no you get nothing! ...before they fall off, you parts will turn "
time.sleep(2)
print(f"Now pick a colour {name} ")
time.sleep(2)
print("select one of the following ")
time.sleep(2)
colour = input("Red(1),\nPurple(2),\nBlue(3),\nGreen(4),\nYellow(5),\nOrange(6)\nPick 1, 2, 3, 4, 5, or 6... ")
if colour == "1":
    colour = "red"
elif colour == "2":
    colour = "purple"
elif colour == "3":
    colour = "blue"
elif colour == "4":
    colour = "green"
elif colour == "5":
    colour = "yellow"
elif colour == "6":
    colour = "orange"
else:
    colour = "into hot scalding mush, and then be placed"
time.sleep(2)
print(F"right then, you now have a {colour} {startingPick1} in your inventory")
time.sleep(2)
print("ok, thats probably enough for now")
time.sleep(2)
print("lets begin!")
#start adventure with a [colour] + statue

#Flashy intro thing "MYSITC BLOOM"

#create a list that corresponds with the random encounter script
#choose an encounter randomly
#remove that number from the list

#i.e
#random encounter
#you come across and old tree with a face
#you can pick an apple
#ask the tree if its alright to pick an apple
#or move on
#outcome 1,2,3


def choice1():
    choice1pick = input("pick a path (1, 2, or 3) ")
    if choice1pick == "1":
        print("you picked path 1")
        path1()
    elif choice1pick == "2":
        print("you picked path 2")
        path2()
    elif choice1pick == "3":
        print("you picked path 1")
        print (choice1)
        path3()
    else:
        print (choice1pick)
        print("please pick either 1, 2, or 3 ")
        choice1()

def path1():
    print("you are on path one")
    time.sleep(2)
    print("walking along the road you see a puddle, with a large green frog resting on a lily pad in its center")
    time.sleep(2)
    print("what will you do")
    path1choice = input("(1) jump in the puddle.\n(2)try to speak to the frog\n(3)pee in the puddle... Pick 1, 2, or 3 ")
    if path1choice == "1":
        print("!ou jump in expecting to splash up to your ankles, but you fall thorugh its surface and now float in frigid, murky waters completely submerged.\n Above you is soft light. \nIn front of you is a large shadowy mass maybe 60ft away from you and quickly getting closer")
        path1_2 = input("what are you gonna do?\n(1)Get the hell out of here!\n(2)Say hello you the giant shadowy mass... \nPlease pick 1, or 2... ")
        if path1_2 == "1":
            print("you swim upwards as fast as you can. break the surface of the puddle and climb out. just in time to see something rush beneath you... that was close! \n right then. continue on your way")
            #function to continue from end of choice 1
        elif path1_2 == "2":
            print("You only see the a flash of teeth before and ecrusiating death... this is where your adventure ends")
            #function to begin the adventure again
        else:
            print("pick either 1 or 2")
            path1()
    if path1choice == "2":
        print("You say 'hello' to the frog. it smiles and warns you of the danger of the puddel\n 'This isnt any ordinary puddle, a monster lurks in its depths. There is a magical gem down there but you will need a powerful ")

def path2():
    print("you are on path two")
    time.sleep(2)
    print("As you walk along, you see a small hutt on the side of the road.\nWhispey streams of bluish smoke carry a sweet smell out between animal hide flaps.")
    time.sleep(2)
    path2Choice1 = input("what would you like to do? \n(1) Poke your head in and have a look\n(2) Dont be rude, walk right past...\n(3)Dont trust this game, burn it to the ground!\nEnter 1 or 2")
    if path2Choice1 == "1":
        print("Your head gets bonked. a wirey witch wearing only a waist high grass skirt stares at you with good eye. ")
    elif path2Choice1 == "2":
        print("you walk past, you know better than to mess with odd huts")
    elif path2Choice1 == "3":
        print("your ill intent is immediatly picked up on.\nThe house grows chicken legs and runs off, \nbut not before covering you in a large ammount of, semi-green, stinky, birdhouse poop")
    else:
        print("Please pick 1, 2, or 3")

def path3():
    print("you are on path three")
    time.sleep(2)
    print("...you die of dysentery")
    choice1()

choice1()

