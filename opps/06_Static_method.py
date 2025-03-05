class Car:
    TotalCars=0
    def __init__(self,Brand,Model):#Constructor self is like this in cpp
        self.__Brand=Brand           #Data members can be written as this
        self.Model=Model
        Car.TotalCars+=1
    # static method->it does not contains self as we have to resirict obect's access to this method
    @staticmethod
    def Full_name():
        print("Means of transport")
    
    def Fuel_type(self):
        if(self.__Brand=="Audi"):
            print("Petrol")
        else:
            print("Hydrogen")
    @property
    def getBrand(self):
        return self.__Brand
    
'''
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
    
        
'''
#My_EV=EV("Audi","Nexon","500KW")
#print(My_EV.Full_info())
My_car=Car("Hundai","Creta")
Car.Full_name() #static method
My_car2=Car("ogga","booga")
print(My_car.Fuel_type())

print(Car.TotalCars)

#Make a datameber read only type using @property decorator and making the data member private
print(My_car.getBrand)
My_car.Brand="sexy"
print(My_car.getBrand)


