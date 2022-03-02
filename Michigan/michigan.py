class PartyAnimal:
    x = 0
    y = 2 + 3
    name = ""
    
    def __init__(self, z):
        self.name = z
        print(self.name , "constructed")
    
    def party(self):
        self.x = self.x + 1
        for i in range(self.x):
            self.y = self.y + self.x + 3.2
        
        print(f"So far {self.x}")
        

    def __del__(self):
        print("I'm self distructed")

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
        
j = FootballFan("Tarokh")
j.party()
j.touchdown()