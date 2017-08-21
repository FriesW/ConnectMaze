class Node:

	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3
	
	__inverse = [BOTTOM, LEFT, TOP, RIGHT]

	def __init__(self):
		self.nodes = self.__init_array(4, None)
		self.connects = self.__init_array(4, False)
		
	def __init_array(self, l, v):
		a = []
		for i in range(l):
			a.append(v)
		return a
		
	def set_node(self, node, dir):
		if self.nodes[dir] != None:
			self.nodes[dir].nodes[self.__inverse[dir]] = None
		self.nodes[dir] = node
		node.nodes[self.__inverse[dir]] = self
	
	def connect_node(self, dir):
		if self.nodes[dir] == None:
			raise IndexError("There is no node to connect to.")
		self.connects[dir] = True
		self.nodes[dir].connects[self.__inverse[dir]] = True
	
	def has_node(self, dir):
		return self.nodes[dir] != None
	
	def is_connected(self, dir):
		return self.connects[dir]
	
	def get_node(self, dir):
		if not self.has_node(dir):
			raise IndexError("Node doesn't exist! First check if it does with is_DIR_node().");
		return self.nodes[dir]
	
	def is_set_to(self, node):
		return node in self.nodes
	
	def is_connected_to(self, node):
		if node not in self.nodes:
			return False
		return self.connects[self.nodes.index[node]]
	
	def connect_to(self, node):
		if node not in self.nodes:
			raise IndexError("There is no node to connect to.")
		self.connect_node(self.nodes.index(node))