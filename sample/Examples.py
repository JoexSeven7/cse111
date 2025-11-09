# # How to write s User-Defined Function
# # def function_name("param1, param2,paramN "):
# # """documentation string"""
# # statement1
# # statement2

# # statementN
# # return value

# import math

# # Define the main function.

# def main():
#   #Get a radius and a height from the user.
#   r = float(input("Enter the radius of a cylinder: "))
#   h = float(input("Enter the height of a cylinder: "))

#   #Call the compute_cylinder_volume function and store its returned value in a variable to use later.
#   v = compute_cylinder_volume(r, h)

# # Print the volume of the cylinder.
#   print(f"Volume: {v: .2f}")


# # Define a function that accepts two parameters. 
# def compute_cylinder_volume(radius, height):
#   """Compute return the volume of cylinder Parameters
#     radius: the radius of the cylinder
#     height: the height of the cylinder
#   """
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height

#   return volume
# main()
def fullname(w1,w2):
  return w1 + ' ' + w2

f=fullname(w2='faith',w1='charity')
print(f)