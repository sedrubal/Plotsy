from plotsy import *

graph = Plotsy()

graph.config([30, 30])

for i in range(6):
    graph.plot([i**2, i], "@")

for i in range(6):
    graph.plot([i, i**2])
    
for i in range(8):
    graph.plot([28 - i, i])
   
for i in range(29):
    graph.plot([i, 29], "%")
    graph.plot([i, 0], "%")
    graph.plot([29, i], "%")
    graph.plot([0, i], "%")

graph.draw()
