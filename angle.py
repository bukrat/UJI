import packages.initialization
import pioneer3dx as p3dx
p3dx.init()
target = 1.5708    # target angle in radians
r = 0.1953 / 2     # wheel radius\
L = 0.33           # axis length
initialEncoder = p3dx.leftEncoder
robotAngle = 0
while robotAngle < target:
    p3dx.move(1.0,-1.0)
    wheelAngle = p3dx.leftEncoder - initialEncoder
    robotAngle = 2 * wheelAngle * r / L
p3dx.stop()