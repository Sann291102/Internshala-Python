##class and object
class CarDesign:
    def __init__(self, Colour, Company):
        self.colour=Colour
        self.company=Company
        
cardesign_1 = CarDesign("Red","Hyundai Creta")
print(cardesign_1.colour,)
print(cardesign_1.company)
cardesign_2 = CarDesign("Blue", "Mercedes Benz E class")
print(cardesign_2.colour)
print(cardesign_2.company)
