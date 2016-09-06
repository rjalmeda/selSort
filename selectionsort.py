import random
from datetime import datetime

def  selSort(varlist):
	startTime  = datetime.now()
	listmin = 0
	minidx = 0
	idx = 0
	minval = varlist[listmin]
	while listmin < len(varlist)-1:
		while  idx < len(varlist):
			if varlist[idx]<minval:
				minval = varlist[idx]
				minidx = idx
				idx += 1
			else :
				idx += 1
		varlist[listmin],varlist[minidx] = varlist[minidx],varlist[listmin]
		print varlist
		listmin += 1
		idx = listmin
		minval = varlist[listmin]
		minidx = idx
	endTime = datetime.now()
	print endTime - startTime
	return varlist

def generate100():
	idx = 0
	mylist = []
	while idx < 100:
		mylist.append(random.randrange(10001))
		idx += 1
	return mylist