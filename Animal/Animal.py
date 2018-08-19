class M:
    def __init__(self):
        a = Animal('dog', 'woof')
        getCry()

class Animal:
    def __init__(self, type, cry):
        self.type = type
        self.cry = cry

    def getType(self):
        return self.type

    def getCry(self):
        return self.cry

