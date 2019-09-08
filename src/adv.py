from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[]),
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

# Make a new player object that is currently in the 'outside' room.
playerInventory = []

roomInventory = []

player = Player('Rocko',room['outside'])
print(player.room)
direction=''

while direction!= 'q':
    direction = input('One: Please enter a command: ')
    if(direction== 'n'):
        print(player.room.n_to)
        if(player.room.n_to is not None):
            player.room = player.room.n_to
            print(player.room)
        else:
            print('you cant move in that direction')
    
    elif(direction== 's'):
        print(player.room.s_to)
        if(player.room.s_to!=None):
            player.room = player.room.s_to
            print(player.room)
        else:
            print('you cant move in that direction')

    elif(direction== 'e'):
        print(player.room.e_to)
        if(player.room.e_to!=None):
            player.room = player.room.e_to
            print(player.room)
        else:
            print('you cant move in that direction')

    elif(direction== 'w'):
        print(player.room.w_to)
        if(player.room.w_to!=None):
            player.room = player.room.w_to
            print(player.room)
        else:
            print('you cant move in that direction')

    elif(direction == 'pi'):
        playerItemName = input('Enter the item name, to your inventory: ')

        playerItemDesc = input('Enter the item decription: ')

        playerInventory.append(Item(playerItemName,playerItemDesc))

        print(f'player Inventory: {playerInventory}')

        player.items = playerInventory    
        
        print(player)

    elif(direction == 'ri'):
        roomItemName = input('Enter the item name, you want to add to a room: ')

        roomItemDesc = input('Enter the item decription, you want to add to a room: ')

        roomInventory.append(Item(roomItemName,roomItemDesc))

        print(f'room Inventory: {roomInventory}')

        player.room.items = roomInventory        

        print(player.room.items)

    elif(len(direction.split(' '))==2):
        command = direction.split(' ')

        if(command[0].lower() == 'get' or command[0].lower() == 'take'):
            print(f'the room inventory is: {player.room.items}')
            print(f'the player inventory is: {player.items}')

            for item in player.room.items:
                if(item.itemName == command[1]):
                    player.room.items.remove(item)
                    print(item.on_take(item.itemName))
                    player.items.append(item)
                    print(item.on_drop(item.itemName))
                else:
                    print(f'item {command[1]} not found')

        elif(command[0].lower() == 'drop'):
            print(f'the room inventory is: {player.room.items}')
            print(f'the player inventory is: {player.items}')

            for item in player.items:
                if(item.itemName == command[1]):
                    player.items.remove(item)
                    player.room.items.append(item)
                    print(item.on_drop(item.itemName))
                else:
                    print(f'item {command[1]} not found')

    elif(direction=='i'):
        print(f'Current inventory of the player is: {player.items}')


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