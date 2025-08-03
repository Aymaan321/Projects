class Vehicle():
    def __init__(self, seats, fare):
        self.fare = fare
        self.seats = seats
    def getfare(self):
        self.fare = self.seats * 100
        return self.fare
    
class Bus(Vehicle):
    def __init__(self, seats, fare):
        super().__init__(fare, seats)
    def getfare(self):
        a = self.fare / 10
        return self.fare*a

seats = 50  
bus = Bus(seats, 0)
print(f"The fare is ${bus.getfare()}")         
