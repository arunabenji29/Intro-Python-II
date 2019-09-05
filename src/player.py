# Write a class to hold player information, e.g. what room they are in
# currently.

# room = Room('room1','room1 description')

# print(room)	

class Player:
	def __init__(self,player,room):
		self.player = player
		self.room = room

	def __str__(self):
		return f"Player: {self.player} is in {self.room.name}.\n {self.room.description}"

	def __repr__(self):
		return f'Player({repr(self.name)}, {repr(self.room)})'	

