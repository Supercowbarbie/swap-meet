from .item import Item
class Electronics(Item):
    def __init__(self, category = "Electronics", condition = None):
        super().__init__(category = "", condition = None)
        self.category = "Electronics"
        self.condition = condition
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
