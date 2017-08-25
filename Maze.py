from Grid import Grid
import random
#from Param_utils import sanitize_seed

def make_maze(xd, yd, seed):
	xd = int(xd)
	yd = int(yd)
	#seed = sanitize_seed(seed)
	
	random.seed(seed)
	
	master = Grid(xd, yd)
	candidates = master.get_all_nodes()
	
	while len(candidates) > 0:
		next = []
		random.shuffle(candidates)
		
		for node in candidates:
			dirs = node.get_valid_directions()
			if len(dirs) > 0:
				dir = random.choice(dirs)
				node.connect_node(dir)
				next.append(node)
		
		candidates = next
	
	return master.printable()