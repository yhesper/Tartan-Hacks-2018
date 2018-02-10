import tkinter
import threading
import time
import user
from sort import *
import os 

# Get all text from another file
# Delete after
allText = []
sortedTag = ["food, eat", "dirty languages", "sleep, rest", "greetings"]

def writeFile(path, contents):
	with open(path, "wt") as f:
		f.write(contents)

def format(d):
	result = ""
	for day in sorted(d.keys()):
		result += "\n\t%d-%d-%d\n" % (day[1], day[2], day[0])
		print (result)
		for text in d[day]:
			result += "\t- "+text.getActualTime()+"-"+text.user+": "+text.content+"\n"
	return result

#d = {(2018,2,3):["hello"],(2018,5,1):["3344"],(2017,3,15):["wuwuwu"]}
#print(format(d))

alltext=[user.Text("user","hello")]

def export(alltext):
	# write a file
	result = ""
	modeList = filterByMode(alltext,[0,1,2])
	for i in range(len(modeList)):
		d = filterByTime(modeList[i])
		newDict = filterBySortingBot(d, sortedTag)
		result += "%s" % user.mode[i]
		result += format(newDict)
		result += "\n"
	return result

def exportToTxt(result,path="Work.txt"):
	writeFile(path, result)

# result = "2015-2-3:\n \t - 5:03: Hello\n \t - 6:03: World!\n"