cars = 100 #defines var cars
space_in_a_car = 4 #defines var space in a car removing the float seems to remove all flaots related to this line
drivers = 30 #defines var drivers
passengers = 90 #defines var passengers
cars_not_driven = cars - drivers #prompts subtraction
cars_driven = drivers #redefines var drivers
carpool_capacity = cars_driven * space_in_a_car #prompts multiplication
average_passengers_per_car = passengers / cars_driven #prompts division
#to create a varaible you simply write an = statemenet DO NOT use ()
#NExt series of lines prints text with the definiatio of specified variables
print("there are" , cars , "cars available.") #defined on line 1
print("There are only", drivers , "drivers available.") # defined on line 3
print("There will be" , cars_not_driven , "empty cars today.") #defined on line 5
print ("We can transport" , carpool_capacity , "people today.") #defined on line 7
print("We have", passengers , "to carpool today.") #defined on line 4
print ("We need to put out about" , average_passengers_per_car , "in each car.") # stems from line 8
# It appears variables must be defined as int and operations prior to prompting a print
