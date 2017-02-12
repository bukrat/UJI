def move(V_robot, w_robot):
    L = 0.33
    r = 0.1953 / 2
    w_r = (2 * V_robot + L * w_robot) / 2 * r
    w_l = (2 * V_robot - L * w_robot) / 2 * r
    p3dx.move(w_r, w_l)
	
import packages.initialization
import pioneer3dx as p3dx
p3dx.init()

# First circle
R = 1
V = 0.35
w = V / R
T = (2 * 3.14 * R) / V
move(V,w)
p3dx.sleep(T)

# Second circle
R = 1
V = 0.35
w = V / R
T = (2 * 3.14 * R) / V
move(V,-w)
p3dx.sleep(T)
# Stop the robot
move(0,0)