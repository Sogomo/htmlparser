from html.parser import HTMLParser
from collections import OrderedDict
import sys
import re
import copy


args = len(sys.argv)
if args > 1:
	pages = []
	wordlist = {}

class MyParser(HTMLParser):

	def handle_data(self, data):
		thisdata = re.sub(r'[^\w\s]', '', data).split()
		mydata.extend(thisdata)

def uniqueLists(myLists):
	uniqueLists = {}
	for key in myLists.keys():
		uniqueLists.update({key: {}})
		myLists[key].sort()
		for item in myLists[key]:
			if item.lower() not in uniqueLists[key].keys():
				uniqueLists[key].update({item.lower(): 0})
			uniqueLists[key][item.lower()] += 1
		
		uniqueLists[key] = sorted(uniqueLists[key].items())
		uniqueLists[key] = dict(uniqueLists[key])

	return uniqueLists


if args > 1:
	for arg in range(1, args):
		mydata = []
		pages.append(sys.argv[arg])
		parser = MyParser()
		uf = sys.argv[arg]
		f = open(uf, "r")
		file = f.read()
		parser.feed(file)
		parser.reset()
		parser.close()
		f.close()
		mydata.sort()
		wordlist[pages[arg-1]] = list(mydata)
		uniqueList = uniqueLists(wordlist)
#	print(uniqueLists(wordlist))
	for items in uniqueList:
		print(uniqueList[items])
		print('\n\n')

else:
	uf = sys.argv[1]
	f = open(uf, "r")
	file = f.read()
	parser.feed(file)
	print(uniqueLists(mydata))


