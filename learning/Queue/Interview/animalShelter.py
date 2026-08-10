class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        
    def enqueue(self, animal, type):
        if type == "dog":
            self.dogs.append(animal)
        elif type == "cat":
            self.cats.append(animal)
            
    def dequeuecat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog =  self.dogs.pop(0)
            return dog
    
    def dequeueAny(self):
        if len(self.dogs) == 0:
            result =  self.cats.pop(0)
        else:
            result =  self.dogs.pop(0)
        return result
    
custom = AnimalShelter()
custom.enqueue("dog1", "dog")
custom.enqueue("cat1", "cat")
custom.enqueue("dog2", "dog")
custom.enqueue("cat2", "cat")
print(custom.dequeuecat())