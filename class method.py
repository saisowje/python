## calling parent class objects in chaild class through super() method 
### writen by sowjanya

class Vehicle:
    vehicle_name = "ADDI A6"
    mileage = 14
    capacity = 4
    price = 750000  

    def __init__(self,vehicle_name,mileage,capacity,price):
        self.vehicle_name = vehicle_name
        self.mileage = mileage
        self.capacity = capacity
        self.price = price

class SubVehicle(Vehicle):
    engine = "SI-Engine"
    chasis_no = 28.457

    def __init__(self,vehicle_name, mileage,capacity,price, engine, chasis_no):
        super().__init__(vehicle_name,mileage,capacity,price) ## must call MRO(method resolving order "left to right") mthod. 
        self.engine = engine
        self.chasis_no = chasis_no

childObj = SubVehicle("jaguar",8,4,900000,"xyzenginee",2750507)
print("vehicle_name:",childObj.vehicle_name)
print("vehicle_mileage:",childObj.mileage)
print("vehicle_capacity:",childObj.capacity)
print("vehicle_price:",childObj.price)
print("vehicle_enginee:",childObj.engine)
print("vehicle_chasis_no:",childObj.chasis_no)