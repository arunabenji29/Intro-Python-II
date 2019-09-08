# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
	def __init__(self,player,room,items=[]):
		self.player = player
		self.room = room
		self.items = items

	def __str__(self):
		if self.items:            
			result =  f'Player: {self.player} is in {self.room.name}.\n {self.room.description}. Items are \n'

			for i in self.items:
				result += f'     item name: {i.itemName} item description: {i.itemDesc}\n'

			return result

		else:
			return f"Player: {self.player} is in {self.room.name}.\n {self.room.description}"

	def __repr__(self):
		return f'Player({repr(self.player)}, {repr(self.room)})'	

