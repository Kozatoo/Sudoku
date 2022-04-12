
from grid import Grid

g=Grid()
g.insertGrid()
g.printGrid()

print("Some Changes!")

g.insertValue(0,1,5)
g.printGrid()
g.insertValue(0,2,5)
g.printGrid()
g.deleteValue(0,1)
g.printGrid()