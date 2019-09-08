# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

# items = [Item('hat','wear on your head'),Item('gloves','wear on your hands'),Item('armour','wear on your chest')]

class Room:
    def __init__(self,name,description,items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'

    def __str__(self):
        if self.items:
            
            result =  f'This is {self.name} has {self.description}. Items are \n'

            for i in self.items:
                result += f'     item name: {i.itemName} item description: {i.itemDesc}\n'

            return result
        else:
            return f'This is {self.name} has {self.description}'



