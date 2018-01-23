# MutateMaze
Experimentation in creating mazes with python.\
Also see: [FriesW/GrowMaze](https://github.com/FriesW/GrowMaze)\
Also see: [FriesW/MutateMaze](https://github.com/FriesW/MutateMaze)

## Use
Created in Python 2.7. To use, simply invoke Run.py. To make mazes in other pieces of software, import make_maze from Maze.py.

## A maze!
This looks okay in a desktop browser, but might not look right on mobile. Apparently mobile github code blocks don't use a monospace font.
```
Maze Hash: ge3hymjtpr3fcu3kn5yhs3tkpa
Dimensions: 16x13
███████████████████████████████████████████████████████████████████████████████████████████████████
███               ███         ███                                                               ███
█████████   █████████   █████████   ███████████████   ███   ███████████████   ███████████████   ███
███   ███                                 ███         ███   ███         ███   ███               ███
███   ███   ███   █████████████████████   ███████████████████████████   █████████   █████████   ███
███         ███   ███         ███   ███               ███                           ███         ███
█████████   ███   █████████   ███   ███   █████████████████████   █████████   ███████████████   ███
███         ███               ███         ███   ███   ███   ███   ███                     ███   ███
███████████████   ███   ███████████████   ███   ███   ███   ███   ███   █████████   █████████   ███
███   ███         ███   ███         ███                     ███   ███         ███   ███         ███
███   ███████████████   ███   ███████████████   ███████████████   █████████   ███████████████   ███
███         ███         ███         ███   ███   ███   ███   ███   ███         ███         ███   ███
███   ███████████████   ███   █████████   █████████   ███   ███   ███   ███████████████   █████████
███               ███   ███         ███                     ███   ███                     ███   ███
███   █████████   █████████   ███   ███   ███████████████   ███   ███   █████████████████████   ███
███         ███   ███         ███               ███   ███         ███                           ███
███████████████   ███   █████████   ███████████████   ███████████████   ███████████████   ███   ███
███         ███   ███   ███   ███               ███         ███         ███         ███   ███   ███
█████████   ███   █████████   █████████   █████████   ███   ███   █████████   █████████   █████████
███         ███         ███   ███         ███   ███   ███                           ███         ███
███   ███   ███   ███   ███   ███   █████████   ███   █████████   ███   █████████   █████████   ███
███   ███         ███   ███         ███   ███         ███         ███         ███   ███         ███
███   █████████   █████████   █████████   █████████   █████████   ███████████████   █████████   ███
███   ███               ███               ███   ███   ███               ███         ███         ███
███████████████   ███████████████   █████████   █████████████████████████████████   █████████   ███
███                                                   ███                           ███         ███
███████████████████████████████████████████████████████████████████████████████████████████████████
```

## How it works
It is similar to GrowMaze. However, any node can be grown at any time. This approach is generally simpler, but is surprisingly difficult to prove it will connect all possible edges. Thus, the maze_maze function continues until all nodes are exhausted. This approach tends to create more random appearing mazes.