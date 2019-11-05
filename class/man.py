# Initialization
class Man:
    def __init__(self, name):
        self.name = name
        print("initial")

    def hello(self):
        print("hello " + self.name)

    def goodbye(self):
        print("Good Bye " + self.name)
m = Man("Saein")
m.hello()
m.goodbye()