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
@ Class my_room() makes the room object using attributes from the source text file.
'''

'''
@ welcome_window() starts the game welcoming the user.
'''

class my_room:
    def __init__(self, name, description, treasures):
        self.name = name
        self.description = description
        self.treasures = treasures

'''
@ room_list() makes the list of available rooms in the source text file.
'''
def room_list():
    lines = file_path.readlines()
    lines = list(lines)
    rooms = []
    read_room = False
    for line in lines:
        line = line.strip() #"weapon\n"
        if read_room:
            room_data = line.split(";")
            rooms.append(my_room(*room_data))
            read_room = False
        if line == "Room":
            read_room = True
    return rooms
