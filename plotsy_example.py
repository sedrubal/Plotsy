from plotsy import *

graph = Plotsy()

graph.config([30, 30])

for i in range(6):
	graph.plot([i**2, i], "@")

for i in range(6):
	graph.plot([i, i**2])

graph.draw()
