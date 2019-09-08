class Item:
    def __init__(self,itemName,itemDesc):
        self.itemName = itemName
        self.itemDesc = itemDesc

    def __str__(self):
        return f'Item Name: {self.itemName}, Item description: {self.itemDesc} '

    def on_take(self,itemName):
        return f'Item {self.itemName} is picked'
    
    def on_drop(self,itemName):
        return f'Item {self.itemName} is dropped'

# item = Item('hat','put on your head')        

# print(item)