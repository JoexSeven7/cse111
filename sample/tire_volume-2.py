import math
from datetime import date

# User inputs informations 
width = float(input("Enter the width of the tire in mm: "))
area= float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Logic behind the program to calulate the results
width_area = width * area

cal_for_diameter = 2540 * diameter

add_Width_and_cal = width_area + cal_for_diameter 

widthsqrt = width ** 2

mulit_widthsqrt_and_area = widthsqrt * area

mulit = mulit_widthsqrt_and_area * add_Width_and_cal

mulit_pi_and_muilt = mulit * math.pi

volume = mulit_pi_and_muilt / 10000000000

print (f"The approximate volume is {volume:.2f} liters")

today = date.today()
with open("volumes.txt", "a") as file:
  file.write(f"{today}, {width}, {area}, {diameter}, {volume:.2f}\n")
print("Data has been saved to volume.txt")
