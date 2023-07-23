cars = 100 #defines var cars
space_in_a_car = 4.0 #defines var space in a car
drivers = 30 #defines var drivers
passengers = 90 #defines var passengers
cars_not_driven = cars - drivers #prompts subtraction
cars_driven = drivers #redefines var drivers
carpool_capacity = cars_driven * space_in_a_car #prompts multiplication
average_passengers_per_car = passengers / cars_driven #prompts division
#to create a varaible you simply write an = statemenet DO NOT use ()
#NExt series of lines prints text with the definiatio of specified variables
print("there are" , cars , "cars available.")
print("There are only", drivers , "drivers available.")
print("There will be" , cars_not_driven , "empty cars today.")
