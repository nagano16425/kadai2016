import os
import sys
from nltk import tokenize
import shelve

files = os.listdir(sys.argv[1]) # file list in dir

for FileName in files: # loop for each file

	f = open(sys.argv[1] + "/" + FileName,"r")
	txt = f.read()
	f.close()
	sh = shelve.open("index.shelve")
	count = {}
	for sent in tokenize.sent_tokenize(txt.strip()):
		for word in tokenize.word_tokenize(sent):
			# for each word
			if word not in sh:
				# add index of word
				sh[word] = len(sh) + 1
				# counter = 1
				count[ sh[word] ] = 1
			else:
				if sh[word] in count:
					# increment counter
					count[ sh[word] ] += 1
				else:
					# word is in shelve, but not in count
					# counter = 1
					count[ sh[word] ] = 1
	sh.close()
	out = []
	out.append(str(sys.argv[2]))
	
	
	for k, v in sorted(count.items(), key = lambda x: int(x[0])):
		out.append("%d:%d" %(k,v))
	print " ".join(out)

