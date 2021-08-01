
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self, sound):
        print(f" This animal says {sound}")
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"
    
class Cat(Animal):
    def __init__(self, breed, fav_toy):
        super().__init__(name, species)
        #Animal.__init__(self, name, species)
        self.breed = breed
        self.toy = fav_toy    
        
blue = Cat("Micky", "cat", "Gavti", "Mouse")
print(blue)