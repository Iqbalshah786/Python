class Car:
    total_car = 0 # solution 6

    def __init__(self,brand,model):
        self.__brand = brand  # make brand private attribute
        self.__model = model
        Car.total_car += 1 # solution 6
    
    def get_brand(self): # solution 4
        return self.__brand + "!"

    def full_name(self): # solution 2
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self): # solution 5
        return "petrol or Diesel"
    
    @staticmethod
    def general_description(): # solution 7
        return "Cars are means of transport"
    
    @property
    def model(self): # solution 8
        return self.__model
    
# solution 3
class ElectricCar(Car): 
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self): # solution 5
        return "Electric Charge"

my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())
print(Car.general_description())

my_new_car = Car("Tata","Safari")
# print("New car brand :",my_new_car.brand)
# print("New car model :",my_new_car.model)
print(my_new_car.full_name())
print(my_car.model)

my_tesla = ElectricCar("Tesla","Model S","85KWH")
# print(my_tesla.__brand) not accessible
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())

print(Car.total_car)

# solution 9
print(isinstance(my_tesla, Car)) 
print(isinstance(my_tesla, ElectricCar))


# solution 10
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())