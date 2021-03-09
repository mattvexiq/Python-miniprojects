class Dog:
    def __init__(self, size, color, breed):
        self.size = size
        self.color = color
        self.breed = breed

    def bark(self, happy):
        #if happy:
        #    print("bark")
        if self.size == "big" and happy:
            print("bark")
        else:
            print("i don't want to bark")



Bob = Dog("big", "golden", "golden retriever") # size, color, breed
Bob.bark(False)