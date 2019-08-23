import time
import random

item = ['dagger']
weapon = ['Flame Sword', 'Katana', 'Hand Grenade', 'Bows and Arrows']
enemy = ["dragon", "wicked fairie", "pirate", "troll", "chucky"]
place = []
weapon = random.choice(weapon)
enemy = random.choice(enemy)

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.", )
    print_pause("Rumor has it that a " + enemy + " is somewhere around "
                "here, and has been terrifying the nearby village")
    print_pause("To your left is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty "
                " (but not very effective dagger)")
    print_pause("\n Enter 1 to knock on the door of the house"
                "\n Enter 2 to peer into the cave"
                "\n What would you like to do?")

def house():
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock "
                    "when the door opens and out steps a " + enemy )
        print_pause("Eep! This is the " + enemy + "house!")
        if "dagger" in item:
            print_pause("you feel a bit under-prepared for this, "
                        "what with only having a tiny dagger.")
            ans = ''
            while ans != "1" and ans != "2":
                ans = input("Would you like to 1 Fight or 2 run away?")
                if ans == "1":
                    print_pause("You feel a bit under-prepared for this, "
                                "what with only having a tiny dagger.")
                    print_pause("You do your best..,but the dagger wasn't help for fighting.")
                    print_pause("You have been defeated!")
                    print_pause("\n \n \t YOU LOSE")
                    play_again()

                if ans == "2":
                    feild()
                    play_again()

        elif weapon in item:
            print_pause("The " + enemy + " attack you \n")
            ans = ''
            while ans != "1" and ans != "2":
                ans = input("Would you like to 1 Fight or 2 run away?\n")
                if ans == "1":
                    print_pause("As the " + enemy + " moves to attack, "
                                "you unsheath your new" + weapon)
                    print_pause("The " + weapon + " of " + enemy +
                                " shines brightly in your hand as you brace "
                                "yourself for the attack.")
                    print_pause("But the " + enemy + " takes one look at "
                                "your shiny new toy and runs")
                    print_pause("You have rid the town of the " + enemy +
                                ". YOU ARE VICTORIOUS!")
                    print_pause("\n \n \t YOU WIN")
                    play_again()

                if ans == "2":
                    feild()
                    print_pause("\n \n \t YOU LOSE")
                    play_again()
        else:
            print_pause("\n \n \t YOU LOSE")
            print_pause([play_again()])

def cave():
    if "cave" not in place:
        print_pause("\n You peer cautiously into the cave")
        print_pause("You've been here before, and gotton all the good stuff"
                    "It's just an empty cave now")
        print_pause("You walk back out to the field")
        play_again()
        print_pause("\nYou peer cautiously into the cave")
        print_pause("It truns out to be only a very small cave")
        print_pause("Your eye catches a glint of metal behind a rock")
        print_pause("You have found the " + weapon + " of " + enemy)
        print_pause("You discard your silly old dagger and "
                    "take the " + weapon + " with you")
        item.remove("dagger")
        item.append(weapon)
        print_pause("You walk back out to the field")
        item.append("cave")
    else:
        print_pause("\n You Peer cautiously into the cave.")
        print_pause("You've been here befor, and gotton all the good stuff."
                    " it's just an empty cave now.")
        print_pause("You walk Back out to the feild.")


def feild():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed")

def play_game():
    ans = ""
    if "started" not in place:
        intro()
        place.append("started")
        while ans != "1" and ans != "2":
            ans = input("\n (Please enter 1 or 2)\n")
            if ans == "1":
                house()
            elif ans == "2":
                cave()
            else:
                play_again()
    else:

        while ans != "1" and ans != "2":
            ans = input("\n (Please enter 1 or 2)\n")
            if ans == "1":
                house()
            elif ans == "2":
                cave()
                intro()
            else:
                play_again()

def play_again():
    ans = input("\n Would you like to play again?\n"
                "If you want to continue to play, enter 1\n"
                "If you want to leave, enter 2\n")
    if ans == "1":
        play_game()
    elif ans == "2":
        print_pause("See you next time!")
    else:
        print_pause("Please Enter 1 or 2")
        play_again()

play_game()