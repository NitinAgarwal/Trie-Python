#!usr/bin/env python

_end = '$'

def insert(root,words):
	current_dict = root
	for word in words:
		count = 0
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})
		if current_dict.has_key(_end):
			count = current_dict[_end]
		current_dict[_end] = count+1
	#print count+1
	return root;

'''
def modify(root):
	current_dic = root;
	if not _end in current_dict:
		current_dict = current_dict.setdefault(_end,1)
	fo letter in current_dict:
		if not letter == _end:
			modify(current_dict[letter]);
''' 

def count(root):
	cnt = 0;
	for letter in root:
		if not letter == _end:
			cnt += count(root[letter]);
	return cnt+1;
		
def num_SubStr(word):
	root = {}
	for i in range(len(word)):
		insert(root,word[i:]);
	return count(root)-1;	
 		
def main():
	testcases = int(raw_input())
	for test in range(testcases):
		num = int(raw_input())
		word = str(raw_input())		
		res = num_SubStr(word)
		print res
	
if __name__ == "__main__":
	main()


