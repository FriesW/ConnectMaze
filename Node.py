class Node:

	TOP = 0
	RIGHT = 1
	BOTTOM = 2
	LEFT = 3
	
	__all     = [ TOP,    RIGHT, BOTTOM, LEFT  ]
	__inverse = [ BOTTOM, LEFT,  TOP,    RIGHT ]

	def __init__(self):
		self.nodes = self.__init_array(4, None)
		self.connects = self.__init_array(4, False)
		self.group_id = object()
		
	def __init_array(self, l, v):
		a = []
		for i in range(l):
			a.append(v)
		return a
	
	def __set_group_id(self, obj):
		if self.group_id != obj:
			self.group_id = obj #Must do first!
			for n in self.nodes:
				if n != None and self.connects[self.nodes.index(n)]: #If exists and connected to
					n.__set_group_id(obj)
	
	def set_node(self, node, dir):
		if self.nodes[dir] != None:
			raise Exception("set_node can only be called once per direction.")#Should make this more specific
		self.nodes[dir] = node
		node.nodes[self.__inverse[dir]] = self
	
	def connect_node(self, dir):
		if self.nodes[dir] == None:
			raise IndexError("There is no node to connect to.")
		if self.group_id == self.nodes[dir].group_id:
			raise Exception("Cannot connect to node in same group.")#Should make this more specific
		self.connects[dir] = True
		self.nodes[dir].connects[self.__inverse[dir]] = True
		self.nodes[dir].__set_group_id(self.group_id)
	
	def has_node(self, dir):
		return self.nodes[dir] != None
	
	def is_connected(self, dir):
		return self.connects[dir]
		
	def is_any_connected(self):
		for conn in self.connects:
			if conn:
				return True
		return False
	
	def get_valid_directions(self):
		out = []
		for i in self.__all:
			if self.nodes[i] != None and \
			 not self.connects[i] and \
			 self.nodes[i].group_id != self.group_id :
				out.append(i)
		return out
	
	def get_node(self, dir):
		if not self.has_node(dir):
			raise IndexError("Node doesn't exist! First check if it does with is_DIR_node().");
		return self.nodes[dir]
	
	
	
	#Remove?
	
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