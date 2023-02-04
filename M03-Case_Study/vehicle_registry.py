# Kyle S. Geltmaker
# Python version 3.11.1
# Vehicle Registry
# A program that accepts user vehicle information input and prints list of information.

# Creates "Vehicle" super class with vehicle type attribute.
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Creates "Automobile" child class with specific vehicle attributes.
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Acquire user vehicle information.
name = input("Please enter your name: ")
vehicle_type = input("Enter the type of vehicle (Car, Van, Truck, Boat, etc): ")
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (Solid or Sunroof: ")

# Define "Automobile" class that inherits from super class and adds vehicle attributes.
vehicle = Automobile(vehicle_type, year, make, model, doors, roof)

# Print results.
print("---" + name + "---")
print("Vehicle type:", vehicle.vehicle_type)
print("Year:", vehicle.year)
print("Make:", vehicle.make)
print("Model:", vehicle.model)
print("Number of doors:", vehicle.doors)
print("Type of roof:", vehicle.roof)