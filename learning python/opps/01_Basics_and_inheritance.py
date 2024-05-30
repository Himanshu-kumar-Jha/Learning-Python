#OPPS IN PYTHON
#create a car class with attributes like brand and modles
class Car:
    def __init__(self,Brand,Model):#Constructor    self i slike this in cpp
        self.Brand=Brand           #Data members can be written as this
        self.Model=Model
    def Full_name(self):
        print(self.Brand)
        print(" ",self.Model)


My_new_car=Car("Audi","Q8")
My_old_car=Car("BMW","X7")
print(My_new_car.Brand)
print(My_old_car.Brand)

My_new_car.Full_name()
My_old_car.Full_name()

#Demonstration of inheritance
class EV(Car):
    def __init__(self,Brand,Model,Battery_size):
        super().__init__(Brand,Model)              #super keyword gives access to class above and we can access it's methods
        self.Battery_size=Battery_size
    
    def Full_info(self):
        return f"{self.Brand} {self.Model} {self.Battery_size}"

My_EV=EV("Tata","Nexon","500KW")
print(My_EV.Full_info())
My_EV.Full_name()

