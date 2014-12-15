import sys

class State(object):
	def __init__(self, size = (0,0) ,Map = 
	"################"+
	"#..............#"+
    	"#.#.###..###.#.#"+
    	"#...#......#...#"+
    	"#.#...#..#...#.#"+
    	"#.#...#..#...#.#"+
   	"#...#......#...#"+
    	"#.#.###..###.#.#"+
    	"#..............#"+
    	"################"):
		self.Map = Map

	def Map(self):
		pass

	def printchar(self,i):
		sys.stdout.write (self.Map[i])
		if i%16 == 15 :
			print

	def get_len(self):
		return len(self.Map)

	def draw(self, display):
		pass

state = State()
print state.get_len()
sys.stdout.write (state.Map[0])
