#!usr/bin/env python

_end = '$'

def insert(root,word):
	current_dict = root
	count=0
	for letter in word:
		current_dict = current_dict.setdefault(letter, {})
	if current_dict.has_key(_end):
		count = current_dict[_end]
	current_dict[_end] = count+1
	print count+1
	return root;

def return_words(trie):
	l = []
	for letter in trie:
		if letter == _end:
			l.append(' '+str(trie[letter]))
		else :
			for i in return_words(trie[letter]):
				l.append(letter + i)
	l.sort()
	return l

def search(trie, word):
	matched = ''
	current_dict = trie
	test = True 
	for letter in word:
		if letter in current_dict:
			matched += letter
			current_dict = current_dict[letter]
		else:
			test = False
			break
	if test and current_dict.has_key(_end):
		print "true " + str(current_dict[_end])
		return 
	pr = 'false'
	for word in return_words(current_dict):
		pr += ' ' + matched + word
	print pr
			

def remove(trie, word):
	letter = _end
	if len(word)>0 :
		letter = word[0]
		if letter in trie:
			remove(trie[letter],word[1:])
			if len(trie[letter]) == 0:
				del trie[letter]
		else:
			print "-1"
	else:
		if letter in trie :
			if trie[letter] > 1: 
				trie[letter] -= 1
				print trie[letter]
			else: 
				del trie[letter]
				print "0"
		else:
			print "-1"
	

def ptrie(trie,level):
	if level == 1:
		print "root"
	current_dict = sorted(trie)
	for letter in current_dict:
		print level*'| ' + letter
		if not letter == _end: 
			ptrie(trie[letter],level+1)

"""
level = 1
def ptrie(trie):
	if level == 1 : print "root"
	current_dict = sorted(trie)
	for letter in current_dict:
		print level*'|' + letter
		if not letter == _end: 
			level +=1
			ptrie(trie[letter])
			level -=1
"""
		
def main():
	trie = {}
	testcases = int(raw_input())
	for test in range(testcases):
		line = str(raw_input())
		print line
		line = line.split(" ")
		if line[0] == "insert":
			insert(trie, line[1])			
		if line[0] == "search":
			search(trie, line[1])
		if line[0] == "remove":
			remove(trie, line[1])
		if line[0] == "ptrie":
			ptrie(trie,1)
	return

if __name__ == "__main__":
	main()

