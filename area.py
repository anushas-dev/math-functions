import math

find_area = input("Enter the object you want to calculate area for: ")
obj_list = ['circle','square','rectangle','triangle','trapezoid','parallelogram']

def circle_area():
    radius = int(input("Enter radius of the circle: "))
    return math.pi*(radius**2)

def square_area():
    side = int(input("Enter side of the square: "))
    return side*side

def rectangle_area():
    side1, side2 = map(int,input("Enter sides of the rectangle: ").split(" "))
    return side1*side2

def triangle_area():
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    return 0.5*(base*height)

def trapezoid_area():
    base1 = int(input("Enter base1: "))
    base2 = int(input("Enter base2: "))
    height = int(input("Enter height: "))
    return 0.5*(base1*base2*height) 

def parallelogram_area():
    side = int(input("Enter side:"))
    height = int(input("Enter height:"))
    return side*height

if find_area.lower() in obj_list:
    if find_area.lower() =='circle':
        print("The area of circle is: ", circle_area())
    if find_area.lower() =='square':
        print("The area of square is: ", square_area())
    if find_area.lower() =='rectangle':
        print("The area of rectangle is: ", rectangle_area())
    if find_area.lower() =='triangle':
        print("The area of triangle is: ", triangle_area())
    if find_area.lower() =='trapezoid':
        print("The area of trapezoid is: ", trapezoid_area())
    if find_area.lower() =='parallelogram':
        print("The area of parallelogram is: ", parallelogram_area())                                        
else: 
    print("Object not found in the standard list")
