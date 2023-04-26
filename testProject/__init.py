

class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Macbook pro")


com1 = Computer("Macbook Pro", 16)
com2 = Computer("Dell Vostro", 8)

com1.config()
com2.config()

