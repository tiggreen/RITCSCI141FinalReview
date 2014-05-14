#Author @tiggreen

class Pet():
	__slots__ = ('name', 'age', 'species')

def __init__(self, nm, ag, sp):
	self.name = nm
	self.age = ag
	self.species = sp
	
def makePet(nm, ag, sp):
	pt = Pet()
	pt.name = nm
	pt.age = ag
	pt.species = sp
	return pt
