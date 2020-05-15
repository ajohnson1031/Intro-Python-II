import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                      "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

TGREEN =  '\033[32m'
TRED = '\033[31m'
TYELLOW = '\033[33m'
ENDC = '\033[m'

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
my_player = Player("", room['outside'])
   
def adv_game(inp=None):
    
    def print_status():
        print(TGREEN + f"\n{my_player.player_name} has moved to the {my_player.current_room.room_name}\n\n{my_player.current_room.description}\n", ENDC)          
    
    if inp == None:
        inp = input("Please enter your name: ").strip()
        my_player.player_name = inp;
        print(TYELLOW + f"Welcome, {inp}! You are currently in the {my_player.current_room.room_name}.\n", ENDC)
        adv_game("")
    else:
        try:
            inp = input("Please choose a valid cardinal direction (N, S, E or W): ").strip().lower()
            while inp != 'q':            
                if inp == "n" and hasattr(my_player.current_room, 'n_to'):
                    my_player.current_room = my_player.current_room.n_to
                    print_status()
                    adv_game(inp)
                    break
                elif inp == "s" and hasattr(my_player.current_room, 's_to'):
                    my_player.current_room = my_player.current_room.s_to
                    print_status()
                    adv_game(inp)
                    break
                elif inp == "e" and hasattr(my_player.current_room, 'e_to'):
                    my_player.current_room = my_player.current_room.e_to
                    print_status()
                    adv_game(inp)
                    break
                elif inp == "w" and hasattr(my_player.current_room, 'w_to'):
                    my_player.current_room = my_player.current_room.w_to  
                    print_status()
                    adv_game(inp)
                    break
                else:                
                    print(TRED + f"\nCan't go that way, {my_player.player_name}!\n", ENDC)
                    adv_game(inp)
                    break
            
        except:
            print("Sorry, game is out of order... :(")
            
        
adv_game()

# 