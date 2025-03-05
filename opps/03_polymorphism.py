#polymorphism using method overloading 
class Car:
    TotalCars=0
    def __init__(self,Brand,Model):#Constructor self is like this in cpp
        self.Brand=Brand           #Data members can be written as this
        self.Model=Model
        Car.TotalCars+=1

    def Full_name(self):
        print(self.Brand)
        print(" ",self.Model)
    
    def Fuel_type(self):
        if(self.Brand=="Audi"):
            print("Petrol")
        else:
            print("Hydrogen")
    
    
class EV(Car):
    def __init__(self,Brand,Model,Battery_size):
        super().__init__(Brand,Model)              #super keyword gives access to class above and we can access it's methods
        self.Battery_size=Battery_size
    
    def Full_info(self):
        return f"{self.Brand} {self.Model} {self.Battery_size}"
    
    def Fuel_type(self):
        if(self.Brand=="Tata"):
            print("Electric")
        else:
            print("Biogas")
    

My_EV=EV("Audi","Nexon","500KW")
print(My_EV.Full_info())
My_car=Car("Hundai","Creta")
My_car2=Car("ogga","booga")
print(My_car.Fuel_type())

print(Car.TotalCars)

#To keep track of how manty cars are mode we can update count whenever constructor is called


