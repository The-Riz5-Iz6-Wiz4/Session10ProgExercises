#function to find temperature in fahrenheit, celsius, kelvin

def convert_temp():
    fahrenheit = float(input("Enter a temperature in fahrenheit: "))
    #####################################
    def convert_celsius(fahrenheit): #find celsius from fahrenheit

        celsius = (5/9) * (fahrenheit - 32)
        return celsius #returning the value of celsius

    def convert_kelvin(celsius): #finding kelvin from celsius

        kelvin = celsius + 273.15
        return kelvin
    ##################################### below is code for the output
    celsiusOut = convert_celsius(fahrenheit)
    kelvinOut = convert_kelvin(celsiusOut)

    print(f"""The temperature in Fahrenheit is: {fahrenheit}
The temperature in Celsius is: {celsiusOut}
The temperature in Kelvin is: {kelvinOut}""")

convert_temp()
