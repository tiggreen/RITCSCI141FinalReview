#Author @tiggreen

def isPower (a, b):
	if (a == 1): 
		return True
	elif ( a % b == 0 and isPower(a/b, b)):
		return True
	else:
		return False

def isPowerIter(a, b):
	while (a != 1 and a % b == 0):
		a = a/b
	return a == 1

def main():
	print(isPowerIter(124, 2))

main()
 