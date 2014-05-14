#Author  @tiggreen
#Prints all the permutations of the given string

def insertEverywhere(c, s):
	retList = []
	for i in range(len(s) + 1):
		temp = s[:i] + c + s[i:]
		retList.append(temp)
	return retList

def insertEverywhereAll(c, L):
	retList = []
	for str in L:
		temp = insertEverywhere(c, str)
		retList += temp
	return retList

		   
def perms(st):
	if st == '':
		return ['']
	else:
		hd = st[0]
		tl = st[1:]
		return insertEverywhereAll(hd, perms(tl))
		
def main():
	print(perms('abc'))

main()