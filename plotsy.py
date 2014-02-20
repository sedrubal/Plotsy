"""
The Module Itself

Source code stuffies:
    The graph variable in the Plotsy class works like this -
    the lists within the outermost list is the Y (these lists
    will be printed on their own lines), and the values in
    those lists are for the X coordinate.
"""

class Plotsy():
	def config(self, size, background = " "):
		#Make "size" useable throughout the object for math
		self.size = size
		#Make  "background" usable throught the object
		self.background = background
		#Create the grid
		self.graph = [[background] * self.size[1] for _ in range(self.size[0])]

	def plot(self, coords, icon = "#"):
		#Set the X position in list Y to the appropriate icon.
		self.graph[coords[1]][coords[0]] = icon

	#Draw the graph.
	def draw(self):
		for i in range(self.size[1]):
		    print("".join(str(x) for x in self.graph[i]))
		    
	#Clear the graph
	def clear(self):
		self.graph = [[self.background] * self.size[1] for _ in range(self.size[0])]
