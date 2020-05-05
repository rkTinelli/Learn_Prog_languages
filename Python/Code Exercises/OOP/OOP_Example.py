class Vehicle():

    def __init__(self,brand_name, color):
        self.brand_name = brand_name
        self.color = color

    def getBrandName(self):
        return self.brand_name


class Cost:

    def __init__(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost


class Car(Vehicle,Cost):

    def __init__(self, brand_name, color, cost, model):
        Vehicle.__init__(self, brand_name, color)
        Cost.__init__(self, cost)
        self.model = model

    def get_Description(self):
        return "Car Name: " + self.getBrandName() + " " + self.model + " Color: " + self.color + " Cost: " + self.cost

car = Car("Audi", "Red", "5000", "r8")
print("Car description:", car.get_Description())
print("Brand name:", car.getBrandName())
print("Cost of the car: ", car.get_cost())