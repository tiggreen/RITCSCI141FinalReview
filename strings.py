#Author: @tiggreen 

def strcmp(str1, str2):
	lst1 = list(str1)
	lst2 = list(str2)
	if (len(lst1) != len(lst2)):
		return False
	for i in range(len(lst1)):
		if lst1[i] !=  lst2[i]:
			return False 
	return True
	
def insertionSort(lst):
	for i in range(1, len(lst)):
		j = i
		while (j > 0 and lst[j-1] > lst[j]):
			lst[j-1], lst[j] = lst[j], lst[j-1]
			j = j-1 
	return lst
		
def main():
	fp = open('file.txt')
	str1 = fp.readline().strip()
	str2 = fp.readline().strip()
	print(strcmp(str1, str2))
	fp.close()
	
	lst = [3, 2, 4, 5, 1, 2, 18, 20, 45, 7, 7, 29, 12] 
	print(insertionSort(lst))

main()