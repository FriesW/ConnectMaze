from Grid import Grid
import random
#from Param_utils import sanitize_seed

def make_maze(xd, yd, seed):
	xd = int(xd)
	yd = int(yd)
	#seed = sanitize_seed(seed)
	
	random.seed(seed)
	
	master = Grid(xd, yd)
	all = master.get_all_nodes()
	
	random.shuffle(all)
	
	for node in all:
		dirs = node.get_valid_directions()
		if len(dirs) > 0:
			dir = random.choice(dirs)
			node.connect_node(dir)
	
	return master.printable()