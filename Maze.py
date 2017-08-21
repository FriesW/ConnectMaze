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
		#print master.printable()
		#raw_input("wait...")
		if not node.is_any_connected():
			dir = random.choice( node.get_valid_directions() )
			node.connect_node(dir)
	
	return master.printable()