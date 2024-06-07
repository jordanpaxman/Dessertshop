from typing import Protocol

class Freeze(Protocol):

    def chill(self):
        ...
    
    def thaw(self):
        ...
    
    def temperature(self) -> str:
        ...

class Freezer:
    def __init__(self):
        self.items = [] # Store the items in the freezer
    
    def chill(self):
      return 'chilling'

    def thaw(self):
      return 'thawing'
    
    def temperature(self) -> str:
      pass
        
    def put(self, item: Freeze):
        item.chill() # Chill the item before putting it in the freezer
        self.items.append(item)
        
    def get(self, name: str):
        # Take the first item that matches the name out of the freezer
        for item in self.items:
            if item.name == name:
                item.thaw() # Thaw the item before taking it out of the freezer
                self.items.remove(item)
                break