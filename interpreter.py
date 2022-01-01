import os

#Defining global variables
arg = ""
paramList = []
pos = 1 #position/"index" in the dictionary

#defining the starting dictionary
maindict = {}

#function to distinguish the first element in a line and seperate it
def formStrings(fulllist):
    global arg
    global paramList
    arg = fulllist[0]
    fulllist.remove(arg)
    paramList = fulllist

def dictL_add():
    global paramList
    global maindict
    maindict[str(len(maindict)+1)] = paramList[0]

def dictL_up():
    global pos
    pos += 1

def dictL_down():
    global pos
    pos -= 1

def dictL_print():
    global pos
    global maindict
    print(maindict[str(pos)])

def dictL_reset():
    global maindict
    maindict = {}

def dictL_jumpToIndex():
    global pos
    global maindict
    jumpval = paramList[0]
    if(int(jumpval) <= len(maindict)):
        pos = jumpval
    else:
        return

def dictL_change():
    global maindict, pos, paramList
    maindict[str(pos)] = paramList[0]

def checkArg(arg):
    global maindict
    global pos

    if(arg.lower() == "add"):
        dictL_add()
    if(arg.lower() == "up" and pos != len(maindict) and maindict != {}):
        dictL_up()
    if(arg.lower() == "dw" and pos != 1 and maindict != {}):
        dictL_down()
    if(arg.lower() == "prn" and maindict != {}):
        dictL_print()
    if(arg.lower() == "rst"):
        dictL_reset()
    if(arg.lower() == "jti" and maindict != {}):
        dictL_jumpToIndex()
    if(arg.lower() == "chng" and maindict != {}):
        dictL_change()


#opening the file
file1 = input("Enter file to open: ")
openfile = open(file1, "r")
lines = openfile.readlines()

#format each line properly
for e in lines:
    stripstring = e.strip()
    splitstring = stripstring.split(" ")
    formStrings(splitstring)
    checkArg(arg)

