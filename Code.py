import math
print("I will find the hypotenuse (longer end of a triangle), if you tell me the other 2 sides of the triangle \n")
a=float(input("What is the value of a? "))
b=float(input("What is the value of b? "))
c=math.sqrt((a**2)+(b**2))
print("The hypotenuse is ",c)
