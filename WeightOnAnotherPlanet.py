#Function for calculating your equivalent weight on another planet

def calc_weight_on_planet(weight, G = 23.1 ): #If no argument is input for G, it will be 23.1

#nested a function. Unsure how to fix unreachable code without the second function

    def mass_to_weight():
        mass = weight/9.8
        new_weight = mass * G
        return new_weight
    Output = mass_to_weight()
    print(Output)

calc_weight_on_planet(120,23.1) #Calling the fucntion, as well as inputting any arguments

