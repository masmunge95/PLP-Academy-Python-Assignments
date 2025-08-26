# Parent class
class Players:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def perform_action(self):
        print(f"{self.name} from {self.team} is doing something...") # Generic placeholder

# Child classes with perform_action overrides for each class
class GoalKeeper(Players):
    def __init__(self, name, team):
        super().__init__(name, team)

    def perform_action(self):
        print(f"{self.name} from {self.team} saves the penalty!")

class Defender(Players):
    def __init__(self, name, team):
        super().__init__(name, team)

    def perform_action(self):
        print(f"{self.name} from {self.team} makes a super tackle!")

class Midfielder(Players):
    def __init__(self, name, team):
        super().__init__(name, team)

    def perform_action(self):
        print(f"{self.name} from {self.team} is controlling the midfield!")

class Striker(Players):
    def __init__(self, name, team):
        super().__init__(name, team)
        
    def perform_action(self):
        print(f"{self.name} from {self.team} scores a goal!")

# Creating player objects
player1 = GoalKeeper("Odhiambo", "Tusker FC")
player2 = Defender("Kibwage", "AFC Leopards")
player3 = Midfielder("Onyango", "Gor Mahia")
player4 = Striker("Omondi", "Harambee Stars")

# Polymorphism using inheritance and for loop
for player in (player1, player2, player3, player4):
    player.perform_action()