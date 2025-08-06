class Car:
    def fuel_type(self):
        raise NotImplementedError("Subclasses must implement fuel_type()")

    def max_speed(self):
        raise NotImplementedError("Subclasses must implement max_speed()")

class BMW(Car):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari(Car):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "350 km/h"

if __name__ == "__main__":
    bmw = BMW()
    ferrari = Ferrari()

    print(f"BMW Fuel Type: {bmw.fuel_type()}")
    print(f"BMW Max Speed: {bmw.max_speed()}")

    print(f"\nFerrari Fuel Type: {ferrari.fuel_type()}")
    print(f"Ferrari Max Speed: {ferrari.max_speed()}")
