#Author @tiggreen

def anagram(str1, str2):
	if (len(str1) != len(str2)):
		return False
	else:
		return sorted(str1) == sorted(str2)

def main():
	print(anagram("angel", "glean"))
	print(anagram("", ""))
	print(anagram("", "a"))

main()
