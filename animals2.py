class Cat:

    def __init__(self):
        self.mood = "neutral"
    
    def speak(self):
        if self.mood == "neutral":
            print("meow")
        elif self.mood == "happy":
            print("purrr")
        elif self.mood == "angry":
            print("hiss!")
        else:
            print("meow")