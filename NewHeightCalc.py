#importing common divisor from math

from math import gcd

#function for adjusting width to fit aspect ratio

def calc_new_height():
    width = int(input("Enter the current width: "))
    height = int(input("Enter the current height: "))
    deswidth = float(input("Enter the desired width: "))
    div = gcd(width, height) #math function to find greatest common divisor

    height_aspect = height/div
    height_multi = deswidth/(width/div) #Getting the aspect ratio and the number it needs to be multilpied by
    new_height = height_multi * height_aspect
    print(new_height)

calc_new_height() #Calling the function

