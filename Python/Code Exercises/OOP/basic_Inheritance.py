class Vehicle():

    def __init__(self,brand_name, color):
        self.brand_name = brand_name
        self.color = color

    def getBrandName(self):
        return self.brand_name

class Car(Vehicle):

    def __init__(self,brand_name, model, color):
        super().__init__(brand_name,color)
        self.model = model

    def get_Description(self):
        return "Car Name: " + self.getBrandName() + self.model + " Color:" + self.color

car = Car("Audi ", "r8", " Red")
print("Car description:", car.get_Description())
print("Brand name:", car.getBrandName())