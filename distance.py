import packages.initialization
import pioneer3dx as p3dx
import math
p3dx.init()
target = 2          # target distance
radius = 0.1953 / 2 # wheel radius
initialEncoder = p3dx.leftEncoder
distance = 0
while distance < target:
    p3dx.move(2.5,2.5)
    angle = p3dx.leftEncoder - initialEncoder
    distance = angle * radius
p3dx.stop()