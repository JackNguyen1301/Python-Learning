class x:
    i = 5
    def __init__(self):
        self.j = 7

    def printMe(self):
        print(self.j)

ObjectA = x()
ObjectB = x()
ObjectA.printMe()
print(ObjectB.i)
