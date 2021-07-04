"""
@Prepared by: Ahmed Bilal

"""

import textwrap
import sys
import time
from datetime import datetime
from character import player_character
from room import *

'''
The below file from below is input file that has specific data about characters and rooms.
'''

file_path = open("game_input.txt", "r")
'''
The below file is written by the program to store key inrofmation about player location and collectables.
'''
file_path_1 = open("game_output.txt", "r")

file_object = open("game_output.txt", "a")
file_object_1 = open("game_output.txt", "w")

def welcome_window():      
    print('*' * 52)
    print ("* Welcome to \"Survival Endeavors\" a text based RPG *")
    print("*         It takes you to a land of adventures!    *")
    print('*' * 52)
    print("                 -: Play :-                  ")
    print("                 -: Help :-                  ")
    print("                 -: Quit :-                  ")
    user_input()

'''
@ user_input() takes basic information from the user to start, exit or help.
'''

def user_input():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    file_object_1.write("Game started @ "+current_time+"\n")
    option = input("> ")
    if option.lower() == ("play"):
        start_screen()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("help"):
        help_menu()		
    while option.lower() not in ['play', 'help', 'quit']:
        print("Invalid command, please try again.")
        welcome_window()
        option = input("> ")
        if option.lower() == ("play"):
            start_screen()
        elif option.lower() == ("quit"):
            sys.exit()
        elif option.lower() == ("help"):
            help_menu()

'''
@ help_menu() provides game operational details to the user.
'''

def help_menu():
    print("")
    print('*' * 52)
    print("Welcome to the HELP Menu")
    print("We are happy to guide you.")
    print("~" * 52)
    print("You need to first build your character.\nSelecting from different options.")
    print("")
    print("You then navigate through different places.\nEach place has treasures and enemies.")
    print("")
    print("Your goal is to collect treasures.\nAttacking enemies and avoiding their traps.")
    print("")
    print("Navigation from one place to another is\nusinf n, s, w, e options")
    print('*' * 52)
    print("    Please select an option to continue.     ")
    print('*' * 52)
    print("                 .: Play :.                  ")
    print("                 .: Help :.                  ")
    print("                 .: Quit :.                  ")
    user_input()

'''
@ start_screen() initializes the game after the user selects 'play'.
'''

def start_screen():
    print ("~" * 52)
    print("""\nWonderland >>> \nThis place is full of strange harmfull creatures\nand valubale objects that you\
  should collect.\n\nFailure is not an option here.\nSelect your Super Hero to ensure your survival.\n\nYour goal is\
 to collect as many objects as you can\nBut keeping yourself safe!!!""")
    print ("~" * 52)
    user_intro()

'''
@ user_intro() takes basic personal information from the user and stores in the output file.
'''

def user_intro ():
    question1 = "Hello there, what is your name?\n"
    for character in question1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    player_name = input("> ")
    file_object.write("Player Name\n"+player_name+"\n")
    if player_name.lower() == ("quit"):
        sys.exit()
    else:
        while player_name.isdigit() or len(player_name) < 2:
            print("Please enter a vlaid name, it should not include a number.")
            player_name = input("> ")
    question2 = "Happy to have you " + player_name + ", get ready to start an\nadventure:\nWhat is your favourite number?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    fav_num = (input("> "))
    if fav_num.lower() == ("quit"):
        sys.exit()
    else:
        while not(fav_num.isdigit()):
            print ("Invalid input. Please enter a number.")
            fav_num = (input("> "))
    file_object.write("Favourite Number\n"+fav_num+"\n")
    question3 = "Alright, " + player_name + ": Now is the time to select your\ncharacter.\n"
    for character in question3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    player_character()
'''
@ move_next() allows the user to go to next room.
'''

def move_next(name):
    super_man = name
    next_option = "Where do you want to move now?\nEnter any of the below directions.\nn, s, e, w\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    direction = input(">")
    if direction.lower() == "quit":
        sys.exit()
    else:
        while True:
            if direction.lower() in ["n", "s", "e", "w"]:
                if direction.lower() == "n":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "s":
                    room = room_list()
                    file_object.write (f"Health\n{super_man.health}\n")
                    file_object.write (f"Moving to:\n{direction.lower()}\n")
                    file_object.write (f"Room\n{room[0].name}\n")
                    next_option = "You are moving to:\n"+room[0].name+"\n"+">"*40+"\n"
                    for character in next_option:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    story_set_1 (super_man)
                elif direction.lower() == "e":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "w":
                    print ("You cannot go that way.")
                    direction = (input("> "))
            else: 
                print ("It is not a valid input. Please enter only,\n n, s, e, w")
                direction = (input("> "))

'''
@ story_set_1() presents the room environment where user can interact, attack and collect different objects.
'''

def story_set_1 (char_name):
    super_man = char_name
    collections = {}
    print ("You are in a dark narrow place.")        
    room = room_list()
    enemy = enemy_list()
    next_option = "This place is called:"+room[0].name+"\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print ('*' * 52)
    print(textwrap.fill(room[0].description, 52))
    print ('*' * 52)
    next_option = "What would you like to do. \nLook, or Move\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while True:
            if option.lower() not in ["look", "move"]:
                next_option = "It is not a valid input. Please enter either look or move."
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
            elif option.lower() == "look":
                print ('~' * 52)
                print ("You have here:\n"+room[0].treasures)
                print ('~' * 52)
                print (f"You should also beware of an enemy:\n{enemy[0].name} \nwho has weapons:\n{enemy[0].weapons}")
                print (f"It has powers:\n{enemy[0].powers}")
                print ('~' * 52)
                break
            elif option.lower() == "move":
                next_option = "You need to first collect something to move.\n"
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
    next_option = "What would you like to do now? \nA. Ask the Joker for advice \nor\nB. Move alone,\nreply with A or B\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while option.lower() not in ["a", "b"]:
            next_option = "It is not a valid input. Please enter either look or move.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            option = (input("> "))    
    if option.lower() == "a":
        print ('^' * 52)
        print ("Bad choice, he is indeed your enemy. His name is\n"+enemy[0].name)
        file_object.write("Encounter with\n"+enemy[0].name+"\n")
        trapped (super_man, enemy[0])
        file_object.write("Attacked by\n"+enemy[0].name+"\n")
        file_object.write(f"Health\n{super_man.health}\n")
        health = super_man.health
        print (f"Your health is now {super_man.health}")
        print ('^' * 52)
    elif option.lower() == "b":
        print ('^' * 52)
        print ("Good move, now you need to Attack")
        collections[room[0].treasures] = 5
        attack (super_man, enemy[0])
        file_object.write("Attacks\n"+enemy[0].name+"\n")
        file_object.write(f"{room[0].treasures}\n")
        file_object.write(f"{collections[room[0].treasures]}\n")
        file_object.write(f"Health\n{super_man.health}\n")
        health = super_man.health
        print ("Congratulations!!!")
        print (f"{super_man.name} collects -|{room[0].treasures}|- and has health now {super_man.health}")
        print ('^' * 52)
    next_option = "Where do you want to move now?\nEnter any of the below directions.\nn, s, e, w\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    direction = input(">")
    if direction.lower() == "quit":
        sys.exit()
    else:
        while True:
            if direction.lower() in ["n", "s", "e", "w"]:
                if direction.lower() == "n":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "s":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "e":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "w":
                    file_object.write (f"Moving to:\n{direction.lower()}\n")
                    file_object.write (f"Room\n{room[1].name}\n")
                    next_option = "You are moving to:\n"+room[1].name+"\n"+">"*40+"\n"
                    for character in next_option:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    story_set_2 (super_man, health, collections)
            else: 
                print ("It is not a valid input. Please enter only,\n n, s, e, w")
                direction = (input("> "))

'''
@ story_set_2() presents the room environment where user can interact, attack and collect different objects.
'''

def story_set_2 (name, num, objects):
    super_man = name
    health = num
    collections = objects
    print ("You are in the middle of an alien land.")
    room = room_list()
    enemy = enemy_list()        
    next_option = "This place is called:"+room[1].name+"\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print ('*' * 52)
    print(textwrap.fill(room[1].description, 52))
    print ('*' * 52)
    next_option = "What would you like to do. \ninvestigate, or sleep\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while True:
            if option.lower() not in ["investigate", "sleep"]:
                next_option = "It is not a valid input. Please enter either investigate or sleep."
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
            elif option.lower() == "investigate":
                print ('~' * 52)
                print ("You have here:\n" +room[1].treasures)
                print ('~' * 52)
                print (f"You should also beware of an enemy:\n{enemy[1].name} \nwho has weapons: \n{enemy[1].weapons}")
                print (f"It has powers:\n{enemy[1].powers}")
                print ('~' * 52)
                break
            elif option.lower() == "sleep":
                next_option = "It is better to first investigate the area, then sleep.\n"
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
    next_option = "What would you like to do now? \nA. Attack the upcoming snake \nor\nB. Climb the nearby tree,\nreply with A or B\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while option.lower() not in ["a", "b"]:
            next_option = "It is not a valid input. Please enter either look or move.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            option = (input("> "))    
    if option.lower() == "a":
        print ('^' * 52)
        print ("Bad choice, the snake bites you badly. It is\n"+enemy[1].name)
        file_object.write("Encuounter with\n"+enemy[1].name+"\n")
        trapped (super_man, enemy[1])
        file_object.write("Attacked by\n"+enemy[1].name+"\n")
        file_object.write(f"Health\n{super_man.health}\n")
        health = super_man.health
        print (f"Your health is now {super_man.health}")
        print ('^' * 52)
    elif option.lower() == "b":
        print ('^' * 52)
        print ("Good move, it is better to get to a save position and then attack")
        collections[room[1].treasures] = 3
        attack (super_man, enemy[1])
        file_object.write("Attacks\n"+enemy[1].name+"\n")
        file_object.write(f"{room[1].treasures}\n")
        file_object.write(f"{collections[room[1].treasures]}\n")
        file_object.write(f"Health\n{super_man.health}\n")
        print (f"Congrats, -<{super_man.name}>- collects -|{room[1].treasures}|- and has now health {super_man.health}")
        print ('^' * 52)
        health = super_man.health
        collections[room[1].treasures] = 3
    next_option = "Where do you want to move now?\nEnter any of the below directions.\nn, s, e, w\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    direction = input(">")
    if direction.lower() == "quit":
        sys.exit()
    else:
        while True:
            if direction.lower() in ["n", "s", "e", "w"]:
                if direction.lower() == "n":
                    file_object.write (f"Moving to:\n{direction.lower()}\n")
                    file_object.write (f"Room\n{room[2].name}\n")
                    next_option = "You are moving to:\n"+room[2].name+"\n"+">"*40+"\n"
                    for character in next_option:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    story_set_3 (super_man, health, collections)
                elif direction.lower() == "s":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "e":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "w":
                    print ("You cannot go that way.")
                    direction = (input("> "))
            else: 
                print ("It is not a valid input. Please enter only,\n n, s, e, w")
                direction = (input("> "))

'''
@ story_set_3() presents the room environment where user can interact, attack and collect different objects.
'''

def story_set_3 (name, num, objects):
    super_man = name
    health = num
    collections = objects
    print ("You are on a narrow wooden bridge.")
    room = room_list()
    enemy = enemy_list()        
    next_option = "This place is called:"+room[2].name+"\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print ('*' * 52)
    print(textwrap.fill(room[2].description, 52))
    print ('*' * 52)
    next_option = "What would you like to do now? \nsearch, or stand\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while True:
            if option.lower() not in ["search", "stand"]:
                next_option = "It is not a valid input. Please enter either look or move."
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
            elif option.lower() == "search":
                print ('~' * 52)
                print ("You have here:\n" +room[2].treasures)
                print ('~' * 52)
                print (f"You should also beware of an enemy:\n{enemy[2].name} \nwho has weapons: \n{enemy[2].weapons}")
                print (f"It has powers:\n{enemy[2].powers}")
                print ('~' * 52)
                break
            elif option.lower() == "stand":
                next_option = "As the time is short so its better to search the area.\n"
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
    next_option = "What would you like to do now? \nA. Catch a small animal in the bush \nor\nB. Focus on crossing the bridge,\nreply with A or B\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while option.lower() not in ["a", "b"]:
            next_option = "It is not a valid input. Please enter either look or move.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            option = (input("> "))    
    if option.lower() == "a":
        print ('^' * 52)
        print ("Bad choice, you get a shocking reply by\n"+enemy[1].name)
        file_object.write("Encounters\n"+enemy[2].name+"\n")
        trapped (super_man, enemy[2])
        file_object.write("Attacked by\n"+enemy[2].name+"\n")
        file_object.write(f"Health\n{super_man.health}\n")
        print (f"Your health is now {super_man.health}")
        print ('^' * 52)
        health = super_man.health
    elif option.lower() == "b":
        print ('^' * 52)
        print ("Smart choice, it's good to keep focused and attack.")
        collections[room[2].treasures] = 2
        attack (super_man, enemy[2])
        file_object.write("Attacks the\n"+enemy[2].name+"\n")
        file_object.write(f"{room[2].treasures}\n")
        file_object.write(f"{collections[room[2].treasures]}\n")
        file_object.write(f"Health\n{super_man.health}\n")
        print (f"Congrats, -<{super_man.name}>- collects -|{room[2].treasures}|- and has now health {super_man.health}")
        print ('^' * 52)
        health = super_man.health
    next_option = "Where do you want to move now?\nEnter any of the below directions.\nn, s, e, w\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    direction = input(">")
    if direction.lower() == "quit":
        sys.exit()
    else:
        while True:
            if direction.lower() in ["n", "s", "e", "w"]:
                if direction.lower() == "n":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "s":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "e":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "w":
                    file_object.write (f"Moving to:\n{direction.lower()}\n")
                    file_object.write (f"Room\n{room[3].name}\n")
                    next_option = "You are moving to:\n"+room[3].name+"\n"+">"*40+"\n"
                    for character in next_option:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    story_set_4 (super_man, health, collections)
            else: 
                print ("It is not a valid input. Please enter only,\n n, s, e, w")
                direction = (input("> "))

'''
@ story_set_4() presents the room environment where user can interact, attack and collect different objects.
'''

def story_set_4 (name, num,  objects):
    super_man = name
    health = num
    collections = objects
    print ("You are in a beautiful lush green garden.")
    room = room_list()
    enemy = enemy_list()        
    next_option = "This place is called:"+room[3].name+"\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print ('*' * 52)
    print(textwrap.fill(room[3].description, 52))
    print ('*' * 52)
    next_option = "What would you like to do now? \nExplore, or Rest\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while True:
            if option.lower() not in ["explore", "rest"]:
                next_option = "It is not a valid input. Please enter either look or move."
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
            elif option.lower() == "explore":
                print ('~' * 52)
                print ("You have here:\n" +room[3].treasures)
                print ('~' * 52)
                print (f"You should also beware of an enemy:\n{enemy[3].name} \nwho has weapons: \n{enemy[3].weapons}")
                print (f"It has powers:\n{enemy[3].powers}")
                print ('~' * 52)
                break
            elif option.lower() == "rest":
                next_option = "Resting without getting the mission accomplished is not a good option.\n"
                for character in next_option:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                option = (input("> "))
    next_option = "What would you like to do now? \nA. Run away from the Dragon \nor\nB. Take position and attack,\nreply with A or B\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    option = input(">")
    if option.lower() == "quit":
        sys.exit()
    else:
        while option.lower() not in ["a", "b"]:
            next_option = "It is not a valid input. Please enter either look or move.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            option = (input("> "))    
    if option.lower() == "a":
        print ('^' * 52)
        print ("Bad choice, you cannot runaway from:\n"+enemy[3].name)
        file_object.write("Encounters\n"+enemy[3].name+"\n")
        trapped (super_man, enemy[3])
        file_object.write("Attacked by\n"+enemy[3].name+"\n")
        file_object.write(f"Health\n{super_man.health}\n")
        print (f"Your health is now {super_man.health}")
        print ('^' * 52)
        health = super_man.health
    elif option.lower() == "b":
        print ('^' * 52)
        print ("Good move, Offence is the right defence!!!")
        collections[room[3].treasures] = 3
        attack (super_man, enemy[3])
        file_object.write("Attacks\n"+enemy[3].name+"\n")
        file_object.write(f"{room[3].treasures}\n")
        file_object.write(f"{collections[room[3].treasures]}\n")
        file_object.write(f"Health\n{super_man.health}\n")
        print (f"Congrats, -<{super_man.name}>- collects -|{room[3].treasures}|- and has now health {super_man.health}")
        print ('^' * 52)
        health = super_man.health
    next_option = "Where do you want to move now?\nEnter any of the below directions.\nn, s, e, w\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    direction = input(">")
    if direction.lower() == "quit":
        sys.exit()
    else:
        while True:
            if direction.lower() in ["n", "s", "e", "w"]:
                if direction.lower() == "n":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "s":
                    file_object.write (f"Moving to\n{direction.lower()}\n")
                    file_object.write (f"Room\n{room[4].name}\n")
                    next_option = "You are moving to:\n"+room[4].name+"\n"+">"*40+"\n"
                    for character in next_option:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    finish_game (super_man, health, collections)
                elif direction.lower() == "e":
                    print ("You cannot go that way.")
                    direction = (input("> "))
                elif direction.lower() == "w":
                    print ("You cannot go that way.")
                    direction = (input("> "))
            else: 
                print ("It is not a valid input. Please enter only,\n n, s, e, w")
                direction = (input("> "))

'''
@ attack() exceutes the attack by the player against the enemy.
'''

def attack (self_name, enemy_name):
    self_name.health = int(self_name.health)
    self_name.health += 2
    enemy_name.health = int (enemy_name.health)
    enemy_name.health -= 2
    print (f"-<{self_name.name}>- uses his -|{self_name.weapons}|- \nto attack his enemy -<{enemy_name.name}>-\
 for a damage -:{enemy_name.health}:-")
    return (self_name, enemy_name)

'''
@ trapped() exceutes the attack by the enemy against the user.
'''

def trapped (self_name, enemy_name):
    self_name.health = int (self_name.health)
    self_name.health -= 2
    enemy_name.health = int (enemy_name.health)
    enemy_name.health += 2
    print (f"-<{enemy_name.name}>- uses his weapon -|{enemy_name.weapons}|- to attack you -<{self_name.name}>- for a\
damage -:{self_name.health}:-")
    return (self_name, enemy_name)

'''
@ finish_game() closes the game publishing the result, final health and the total collectables.
'''

def finish_game(name, num, objects):
    super_man = name
    health = int(num)
    collections = objects
    room = room_list()
    print ("You are about to go back to your world.")
    next_option = "This place is called:"+room[4].name+"\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print ('*' * 52)
    print(textwrap.fill(room[4].description, 52))
    print ('*' * 52)
    print ('~' * 52)
    print (f"Final Health: {health}")
    print ('~' * 52)
    file_object.write (f"Final Health\n{health}\n")
    print ('~' * 52)
    if health >= 10:
        print (f"Congratulations!!! {super_man.name}, You won the game.")
        print ('~' * 52)
        print(f"Total Collections are:\n")
        file_object.write(f"{super_man.name}, You won the game.\n")
        file_object.write(f"Total Collections\n")
        for item, num in collections.items():
            file_object.write(f"{item}: {num}\n")
            print(f"{item}: {num}\n")
    else:
        print ('~' * 52)
        print (f"Sorry, {super_man.name}: you lost!!!")
        print (f"Final health: {super_man.health}")
        file_object.write(f"{super_man.name}, you lost!!!\n")
        print(f"Total Collections")
        file_object.write(f"Total collections:\n")
        if collections:
            for item, num in collections.items():
                file_object.write(f"{item}: {num}\n")
                print(f"{item}: {num}")
        else:
            file_object.write(f"Collections: 0\n")
            print(f"Collections: 0")
    print ('~' * 52)
    file_object.write(f"End Game<>\n")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    file_object.write("Game finished @ "+current_time+"\n")
    file_object.close()
    sys.exit()

'''
@ char_data() reads the player character data from the output file in order to re-load from the unfinished level.
'''
def char_data():
    lines = file_path.readlines()
    lines = list(lines)
    read_superman = False
    for line in lines:
        line = line.strip()
        if read_superman:
            char_data = str(line.split(";"))
            read_superman = False
        if line == "Selected Character":
            read_superman = True
    return char_data

'''
@ weapon_data() reads the player weapon data from the output file in order to re-load from the unfinished level.
'''

def weapon_data():
    lines = file_path.readlines()
    lines = list(lines)   
    read_weapon = False
    for line in lines:
        line = line.strip()
        if read_weapon:
            weapon_data = line.split(";")
            read_weapon = False
        if line == "Selected Weapon":
            read_weapon = True
    return weapon_data

'''
@ pow_data() reads the player power data from the output file in order to re-load from the unfinished level.
'''

def pow_data():
    lines = file_path.readlines()
    lines = list(lines) 
    read_pow = False
    for line in lines:
        line = line.strip()
        if read_pow:
            pow_data = line.split(";")
            read_pow = False
        if line == "Selected Power":
            read_pow = True
    return pow_data

'''
@ health_data() reads the player health data from the output file in order to re-load from the unfinished level.
'''

def health_data():
    lines = file_path.readlines()
    lines = list(lines) 
    read_health = False
    for line in lines:
        line = line.strip()
        if read_health:
            health_data = line.split(";")
            read_health= False
        if line == "Health":
            read_health = True
    return health_data[-1]

'''
@ object_data() reads the player collectables data from the output file in order to re-load from the unfinished level.
'''

def object_data():
    objects = []
    collections = {}
    lines = file_path.readlines()
    lines = list(lines) 
    read_object = False
    for line in lines:
        line = line.strip()
        if read_object:
            object_data = line.split(";")
            objects.append(object_data)
            new_list = ["Gold Coins", "Antique Plates", "Golden Fruits", "Lively roses"]
            for i in range (len(objects)):
                if new_list:
                    a = (objects[i])
                    for b in a:
                        int (b)
                    collections[new_list[i]] = b
                read_object= False
        if line == "Gold Coins" or line == "Antique Plates" or line == "Golden Fruits" or line == "Lively roses":
            read_object = True
    return collections

'''
@ resume_play() helps the user to resume an unfinished game at a later stage.
'''

def resume_play():
    lines = file_object.readlines()
    lines = list(lines) 
    read_room = False
    for line in lines:
        line = line.strip()
        if read_room:
            current_room = line.split(";")
            read_room = False
        if line == "Room":
            read_room = True
    repeat_player = my_character(char_data(), weapon_data(), pow_data(), health_data())
    if current_room == []:
        move_next(repeat_player)
    elif current_room == ['Dark Tunnel']:
        story_set_1 (repeat_player)
    elif current_room == ['Mysterious Land']:
        story_set_2 (repeat_player, health_data(), object_data())
    elif current_room == ['Valley of Death']:
        story_set_3 (repeat_player, health_data(), object_data())
    elif current_room == ['Paradize Land']:
        story_set_4 (repeat_player, health_data(), object_data())
    elif current_room == ['Reward Land']:
        finish_game (repeat_player, health_data(), object_data())

'''
Here it is decided whether to start a new game or resume an unfinished one.
'''
lines = file_path_1.readlines()
if len(lines) > 16 and len(lines) < 66:
    resume_play()
else:
    welcome_window()
