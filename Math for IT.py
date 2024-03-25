"""Math for IT"""
import math
def circle():
    """Math for IT"""
    radius = float(input())
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    print("Area: %.3f"%area)
    print("Circumference: %.3f"%circumference)

circle()
