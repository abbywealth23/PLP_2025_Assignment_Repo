#Assignment 1
class House:
        def __init__(self, type, block, streetName):
                self.type = type
                self.block = block
                self.streetName = streetName

class Apartment(House):
                pass

house1 = House("Bungalow", 3, "Ayonuga,fadeyi")
house2 = Apartment("2-StoreyBuilding", 15, "Allen Avenue")

print(house1.block)
print(house2.streetName)



#Activity 2

class Car:
    def move(self):
      return "Driving!"

class Plane:
   def move(self):
      return "Flying!"  
          
for animal in [Car(), Plane()]:
  print(animal.move())
  

