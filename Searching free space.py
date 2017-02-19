import packages.initialization
import pioneer3dx as p3dx
p3dx.init()

minLeftSensors = min(p3dx.distance[0:3])
maxLeftSensors = max(p3dx.distance[0:3])

minRightSensors = min(p3dx.distance[5:])
maxRightSensors = max(p3dx.distance[5:])

if minLeftSensors > minRightSensors:
    while max(p3dx.distance[3:5]) < (max(p3dx.distance[5:]) or max(p3dx.distance[0:3])):
        p3dx.move(-1,1)
else:
    while max(p3dx.distance[3:5]) < (max(p3dx.distance[5:]) or max(p3dx.distance[0:3])):
        p3dx.move(1,-1)
p3dx.stop()