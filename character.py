import textwrap
import sys
import time

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


'''
@ my_character class is to create characters taking input from the player in the form of name, weapon and powers.
Health is taken as self defined argument (a number 10)
'''

class my_character:
    def __init__ (self, name, weapons, powers, health):
        self.name = name
        self.weapons = weapons
        self.powers = powers
        self.health = health

'''
@ char_list() makes the list of available characters in the source text file.
'''
def char_list():
    lines = file_path.readlines()
    lines = list(lines)
    supermans = []
    read_superman = False
    for line in lines:
        line = line.strip()
        if read_superman:
            superman_data = line.split(";")
            supermans.append(superman_data)
            read_superman = False
        if line == "Superman":
            read_superman = True
    return supermans

'''
@ wep_list() makes the list of available weapons in the source text file.
'''

def wep_list():
    lines = file_path.readlines()
    lines = list(lines)
    weapons = []
    read_weapon = False
    for line in lines:
        line = line.strip()
        if read_weapon:
            weapon_data = line.split(";")
            weapons.append(weapon_data)
            read_weapon = False
        if line == "Weapons":
            read_weapon = True
    return weapons

'''
@ pow_list() makes the list of available powers in the source text file.
'''

def pow_list():
    lines = file_path.readlines()
    lines = list(lines)
    powers = []
    read_pow = False
    for line in lines:
        line = line.strip()
        if read_pow:
            pow_data = line.split(";")
            powers.append(pow_data)
            read_pow = False
        if line == "Powers":
            read_pow = True
    return powers

'''
@ enemy_list() makes the list of available enemies in the source text file.
'''

def enemy_list():
    lines = file_path.readlines()
    lines = list(lines)
    enemies = []
    read_enemy = False
    for line in lines:
        line = line.strip()
        if read_enemy:
            enemy_data = line.split(";")
            enemies.append(my_character(*enemy_data))
            read_enemy = False
        if line == "Enemy":
            read_enemy = True
    return enemies

'''
@ select_char() allows the user to select favourite character name.
'''

def select_char ():
    next_option = "You have to select from any of the 4 super heroes."+ "\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('*' * 52)
    for i, char in enumerate(char_list()):
        print (f"Character No. {i+1} \t{char}")       
    next_option = "Please select your favourite character by typing\n1, 2, 3 or 4\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    fav_char = (input("> "))
    if fav_char.lower() == ("quit"):
        sys.exit()
    else:
        while fav_char not in ["1", "2", "3", "4"]:
            next_option = "It is not a valid input.\nPlease enter a number from 1 to 4.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            fav_char = (input("> "))
    j = int(fav_char) - 1
    a = char_list()[j]
    super_char = ' '.join([str(elem) for elem in a])
    file_object.write("Selected Character\n"+super_char+"\n")
    next_option = "You have selected: "+str(super_char)+"\nWell Done, Good Choice!!!\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)    
    print ('*' * 52)
    return super_char

'''
@ select_wep() allows the user to select favourite weapon name.
'''

def select_wep():
    next_option = "You have to select from any of the 4 super weapons."+ "\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('*' * 52)
    for i, char in enumerate(wep_list()):
        print (f"Character No. {i+1} \t{char}")
    next_option = "Please select your favourite weapon by typing\n1, 2, 3 or 4\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    fav_char = (input("> "))
    if fav_char.lower() == ("quit"):
        sys.exit()
    else:
        while fav_char not in ["1", "2", "3", "4"]:
            next_option = "It is not a valid input.\nPlease enter a number from 1 to 4.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            fav_char = (input("> "))
    j = int(fav_char) - 1
    a = wep_list()[j]
    super_weapon = ' '.join([str(elem) for elem in a])
    file_object.write(f"Selected Weapon\n{super_weapon}\n")
    next_option = "You have selected: "+super_weapon+"\nWell Done, Good Choice!!!\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)    
    print ('*' * 52)    
    return super_weapon

'''
@ select_pow() allows the user to select required power.
'''

def select_pow():
    next_option = "You have to select from any of the 4 powers."+ "\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('*' * 52)
    for i, char in enumerate(pow_list()):
        print (f"Character No. {i+1} \t{char}")
    next_option = "Please select your wanted power by typing\n1, 2, 3 or 4\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    fav_char = (input("> "))
    if fav_char.lower() == ("quit"):
        sys.exit()
    else:
        while fav_char not in ["1", "2", "3", "4"]:
            next_option = "It is not a valid input.\nPlease enter a number from 1 to 4.\n"
            for character in next_option:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            fav_char = (input("> "))
    j = int(fav_char) - 1
    a = pow_list()[j]
    super_power = ' '.join([str(elem) for elem in a])
    file_object.write(f"Selected Power\n{super_power}\n")
    next_option = "You have selected: "+super_power+"\nWell Done, Good Choice!!!\n"
    for character in next_option:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)    
    print ('*' * 52)
    return super_power

'''
@ player_character() makes the object super_man from classe my_character taking inputs from the user.
'''

def player_character():
    super_man = my_character(select_char(), select_wep(), select_pow(), 10)
    return super_man

