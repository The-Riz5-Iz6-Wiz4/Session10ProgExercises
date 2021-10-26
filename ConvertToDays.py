#function for inputting values and converting the values into days

def convert_to_days():
    hours = float(input("Enter number of hours: "))
    minutes = float(input("Enter number of minutes: "))
    seconds = float(input("Enter number of seconds: ")) #All local variables.

    # function for converting hours, minutes, seconds into days

    def get_days():
        HourDay = hours / 24
        MinDay = minutes / 1440
        SecDay = seconds / 86400
        TotalDay = HourDay + MinDay + SecDay
        rounday = round(TotalDay, 4) #rounding to 4 sigfig
        return rounday #Returning the value
    FinalDays = get_days()
    print(FinalDays)

convert_to_days() #Calling the function