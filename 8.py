class LinkedList():
	__slots__= ('head', 'size')

def mkMyList():
    lst = LinkedList()
    lst.head = mkEmpty()
    lst.size = 0
    return lst
	
class Node():
	__slots__ = ('data', 'next')

def mkNode(d, n):
	n = Node()
	n.data = d
	n.next = n
	return n

class EmptyNode():
	__slots__= ()

def mkEmptyNode():
	return EmptyNode()

# time complexity is O(n)
# where n is the number of the nodes in
# the LinkedList	
def maxNode(anyList):
	head = anyList.head
	currMax = head.value
	
	while head.next != anyList.head:
		tempVal = head.next.value
		if (tempVal > currMax):
			currMax = tempVal
		head = head.next
	return currMax

 
#time complexity is O(n)
def append(anyList, value):
	anyList.size += 1
	if isinstance(anyList.head, EmptyNode):
		newNode = mkNode(value, mkEmptyNode())
		anyList.head = newNode
	else:
		currHead = anyList.head
		while (currHead.next != anyList.head):
			currHead = currHead.next
		currHead.next = mkNode(value, currHead.next)
	
	
	