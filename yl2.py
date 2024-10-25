# yl2.py pi = 3.14
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

import math

radius = float(input("radius:"))
surface_area =  (math.pi * (radius*radius))
circumference = (2* math.pi*radius)

print("radius",radius)
print("circumference",circumference)
print("surface_area",surface_area)
