import packages.initialization
import pioneer3dx as p3dx
p3dx.init()

def forward():
    # copy and paste your code here
    target = 2          # target distance
    radius = 0.1953 / 2 # wheel radius
    initialEncoder = p3dx.leftEncoder
    Kp = 2
    power = 2.5
    distance = 0
    error = 0
    while distance < target:        
        error = (p3dx.rightEncoder - turnAngle) - (p3dx.leftEncoder + turnAngle)
        u = error * Kp
        p3dx.move(power + u, power - u)
        angle = p3dx.leftEncoder - initialEncoder
        distance = angle * radius
    p3dx.stop()
	
def turn():
    # copy and paste your code here
    target = 1.5708    # target angle in radians
    r = 0.1953 / 2     # wheel radius
    L = 0.33           # axis length
    global turnAngle
    initialEncoder = p3dx.leftEncoder
    robotAngle = 0
    while robotAngle < target:
        p3dx.move(1.0,-1.0)
        wheelAngle = p3dx.leftEncoder - initialEncoder
        robotAngle = 2 * wheelAngle * r / L
    turnAngle = turnAngle + wheelAngle
    p3dx.stop()
	
print('Pose of the robot at the start')
p3dx.pose()
turnAngle = 0
for _ in range(4):
    forward()
    turn()
print('Pose of the robot at the end')
print turnAngle
p3dx.pose()


%matplotlib inline                
import matplotlib.pyplot as plt   # WARNING: the first time, this import can take up to 30 seconds
x, y = p3dx.trajectory()          # because of font cache building, please be patient and wait
plt.plot(x,y);