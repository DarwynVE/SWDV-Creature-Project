import random

class Creature:
    creatures = ["T-Rex", "Unicorn", "Raptor", "Spinosaurus"]
    
    def __init__(self):
        print("Hey there! Welcome to the Creature Creation Project.")
        print("Please select two creatures from this list:")
        for creature in self.creatures:
            print(creature)
    
    def creatureCheck(self):
        health = random.randrange(100, 1000, 50)
        weight = random.randrange(2, 10)
        strength = random.randrange(1, 100, 2)
        firstOption = input("Choose your first creature: ")
        if firstOption not in self.creatures:
            print("Please Select One Of The Creatures From The List.")
        else:
            secondOption = input("Choose your second creature: ")
            if secondOption not in self.creatures and secondOption != firstOption:
                print("Please Select One Of The Creatures From The List That You Did Not Choose.")
            else:
                self.creation = f"{firstOption[0:3]}{secondOption[4:]}" # Stores the users creation
                print("Congratulations! You have created a", f"{self.creation}.")
                print("Here are some basic stats for your creation.")
                print("Health Points: ", health)
                print("Weight: ", weight, "Tons")
                print("Strength:", strength)
                return self.creation
    
    def ascii(self):
        if hasattr(self, 'creation'):
            print(f"Here is a picture of your {self.creation}.")
            if self.creation == "T-Rorn" or "Unix":
                print("\ \n e-e         \n(\_/)\       \n `-'\ `--.___\n    '\( ,_.-'\n       '\ '\    \n")
            elif self.creation == "T-Ror" or "Rapx":
                print("(\_/)\       \n `-'\ `--.___\n    '\( ,_.-'\n       '\ '\    \n")
                
        
                
creature_creator = Creature()
creature_creator.creatureCheck()
creature_creator.ascii()    