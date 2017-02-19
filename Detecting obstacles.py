import packages.initialization
import pioneer3dx as p3dx
p3dx.init()
eof = "False"
while eof == "False":
    p3dx.move(2.5,2.5)
    if p3dx.distance[3] <= 1 and p3dx.distance[4] <= 1:
        eof = "True"
p3dx.stop()