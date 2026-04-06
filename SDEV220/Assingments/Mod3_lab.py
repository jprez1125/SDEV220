#Jennifer Perez
#app that will accept user input for a car,The app will then ask the user for the year, make, model, doors, and type of roof
#The app will then output the data

#superclass called Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
#subclass called Automobile that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#app to accept user input for a car
def main():
    vehicle_type = "car"
    #ask user for car details
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    #create car object using the Automobile class
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    #outputs the result
    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")
#run the main function
main()