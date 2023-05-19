# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle_area(radius):
    return math.pi * radius**2

# Prompt the user for input
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = calculate_circle_area(radius)

# Display the result
print("The area of the circle is:", area)

