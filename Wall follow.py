import packages.initialization
import pioneer3dx as p3dx
p3dx.init()

MIN_WALL_THRESHOLD = 0.3
MAX_WALL_THRESHOLD = 0.4

DEF_X_SPEED = 0.2       # default forward velocity
DEF_YAW_SPEED = 0.15    # default turning velocity

def move(V_robot,w_robot):
    r = 0.1953 / 2
    L = 0.33
    w_r = (2 * V_robot + L * w_robot) / (2*r)
    w_l = (2 * V_robot - L * w_robot) / (2*r)
    p3dx.move(w_l, w_r)

def getSonars():
    leftSide = min(p3dx.distance[0:3])
    frontSide = min(p3dx.distance[3:5])
    return leftSide, frontSide

def getWall():
    leftSide, frontSide = getSonars()
    # move forward until an obstacle is detected at the front
    while frontSide > MIN_WALL_THRESHOLD:       
        move(DEF_X_SPEED,0)
        leftSide, frontSide = getSonars()
        
    # turn until the wall is detected by sonar 0
    while leftSide > MIN_WALL_THRESHOLD:
        if leftSide > frontSide:
            yawSpeed = -DEF_YAW_SPEED * 3
        else:
            yawSpeed = -DEF_YAW_SPEED
        move(0,yawSpeed)
        leftSide, frontSide = getSonars()
    move(0,0)

try:
    getWall()
    while True:
        leftSide, frontSide = getSonars()
        # by default, just move forward
        xSpeed = DEF_X_SPEED
        yawSpeed = DEF_X_SPEED
        # if we're getting too close to the wall with the front side...
        if frontSide < MAX_WALL_THRESHOLD:
            # go backward and turn right quickly (x4)
            xSpeed = -0.1
            yawSpeed = -0.15 * 4
        else:
            # if we're getting too close to the wall with the left side...
            if leftSide < MAX_WALL_THRESHOLD:
                # move slowly forward (x0.5) and turn right
                xSpeed  = 0.3 * 0.5
                yawSpeed = 0.1 * 0.5
            else:
                # if we're getting too far away from the wall with the left side...
                if leftSide > MAX_WALL_THRESHOLD:
                    # move slowly forward (x0.5) and turn left
                    xSpeed  = 0.15 * 0.5
                    yawSpeed = 0.3 * 0.5
        # Move the robot
        move(xSpeed,yawSpeed)
except KeyboardInterrupt:
    move(0,0)