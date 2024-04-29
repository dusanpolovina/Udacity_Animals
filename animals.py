class Dog:
    
    scientific_name = "Canis lupus familiaris"
    
    def __init__(self, whas):
        self.name = whas
        self.woofs = 0

    def speak(self):
        print("Woof!")
        
    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")
            
    #def learn_name(self, whas):
     #   self.name = whas
        
    def hear(self, sound):
        if "syrus" in sound.lower():
            print("woof!")

    def count(self):
        self.woofs += 1
        for counts in range(self.woofs):
            self.speak()

