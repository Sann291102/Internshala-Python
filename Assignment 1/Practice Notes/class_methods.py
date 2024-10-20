class Car:
    cars=999999
    def __init__(self, name ,Colour, Company, Model, Registration):
        self.name=name
        self.colour=Colour
        self.company=Company
        self.model=Model
        self.reg=Registration
        
            
car_1=Car("Raaju", "Red", "Hyundai", "Creta SX(O,)", "TS05EY2229")
print(car_1.name)
print(car_1.colour)
print(car_1.company)
print(car_1.model)
print(car_1.reg)
print(car_1.cars)
car_2=Car("Vivek", "White", "Audi", "Audi R8", "TG 1  0001")
print(car_2.name)
print(car_2.colour)
print(car_2.company)
print(car_2.reg)
print(car_2.model)