import packages.initialization
import pioneer3dx as p3dx
p3dx.init()
def move(V_robot,w_robot):
	r = 0.1953 / 2\n",
	L = 0.33\n",
	w_r = (2 * V_robot + L * w_robot) / (2*r)
	w_l = (2 * V_robot - L * w_robot) / (2*r)
	p3dx.move(w_l, w_r)

def forward():
	eof = "False"
	while eof == "False":
		p3dx.move(2.5,2.5)
		if p3dx.distance[3] <= 1 and p3dx.distance[4] <= 1:
			eof = "True"
	p3dx.stop()
	
def turn():
	min_lat_dist = 2
	minLeftSensors = min(p3dx.distance[0:3])
	minRightSensors = min(p3dx.distance[5:])

	if minLeftSensors > minRightSensors:
		while (min(p3dx.distance[3:5]) < max(minLeftSensors,0.5)) or (p3dx.distance[6] < min_lat_dist) or (p3dx.distance[7] < 0.1):
			p3dx.move(-2,2)
	else:
		 while (min(p3dx.distance[3:5]) < max(minRightSensors,0.5)) or (p3dx.distance[2] < min_lat_dist) or (p3dx.distance[0] < 0.1):
			p3dx.move(2,-2)
	p3dx.stop()

try:
	while True:
		forward()
		turn()
except KeyboardInterrupt:
	p3dx.stop()
