#Author @tiggreen

class LinkedList():
	__slots__ = ('head', 'size')

class Empty():
	__slots__= ()

class NonEmpty():
	__slots__= ('data', 'next')

def mkNonEmpty(dt, nt):
	nd = NonEmpty()
	nd.data = dt
	nd.next = nt
	return nd

def mkEmpty():
	return Empty()

def mkMyList():
    
    lst = LinkedList()
    lst.head = mkEmpty()
    lst.size = 0
    return lst

"""
Inserts the value into the list 
at the given pos (index).

Precondition: 0 <= lst.size > pos 
"""	
	
def insert (lst, val, pos):
	#let's first create the node we want 
	#to insert into the list. 
	newNode = mkNonEmpty (val, mkEmpty())
	lst.size += 1 
	# If lst is empty
	if isinstance (lst.head, Empty):
		lst.head  = newNode 
	elif isinstance (lst.head, NonEmpty):
		# the node becomes the new head
		if pos == 0:
			temp = lst.head
			newNode.next = temp
			lst.head = newNode
		elif pos > 0:
			curNode = lst.head
			curpos = 0
			while (curpos < pos - 1 and not isinstance (curNode.next, Empty)):
				curNode = curNode.next
				curpos += 1
			
			tempNode = curNode.next
			newNode.next = tempNode
			curNode.next = newNode
		else:
			raise TypeError("Bad List position: " + str(pos))
				
		
		
		
def main():
	lst = mkMyList()
	insert(lst, 7, 0)
	insert(lst, 10, 1)
	insert(lst, 12, 2)
	insert(lst, 26, 3)
	
	while (not isinstance (lst.head, Empty)):
		print(str(lst.head.data) + "->"), 
		lst.head = lst.head.next 

main()
