class Car:
    def __init__(self,Brand,Model):#Constructor    self i slike this in cpp
        self.Brand=Brand           #Data members can be written as this
        self.Model=Model
    def Full_name(self):
        print(self.Brand)
        print(" ",self.Model)

class battery:
    def battery_info(self):
        return "This is a battery"
class Engine:
    def Engine_info(self):
        return "This requires fuel"
class Car_two(battery,Engine,Car):
    pass

My_fav_car=Car_two("Tesla","Model S")
print(My_fav_car.battery_info())
print(My_fav_car.Engine_info())


