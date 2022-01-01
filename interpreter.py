import os

#Defining global variables
arg = ""
paramList = []
pos = 1 #position/"index" in the dictionary
pushvar = 0

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
    global pos, maindict, paramList
    fullprint = ""
    if(paramList[0] != ""):
        print(maindict[str(paramList[0])])
        return
    elif("!lit" in paramList):
        for e in paramList:
            if(e != "!lit"):
                fullprint += e + " "
        print(fullprint)
        return
    print(maindict[str(pos)])

def dictL_reset():
    global maindict
    maindict = {}

def dictL_jumpToIndex():
    global pos, maindict, paramList
    jumpval = paramList[0]
    if(int(jumpval) <= len(maindict)):
        pos = jumpval
    else:
        return

def dictL_change():
    global maindict, pos, paramList
    maindict[str(pos)] = paramList[0]

def dictL_pushIndex():
    global pos, pushvar
    pushvar = pos

def dictL_popIndex():
    global pos, pushvar
    if(pushvar != 0):
        pos = pushvar
        pushvar = 0

def dictL_printAll():
    global maindict
    for e in maindict:
        print(e + " : " + maindict[e])

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
    if(arg.lower() == "pushi" and maindict != {}):
        dictL_pushIndex()
    if(arg.lower() == "popi" and maindict != {}):
        dictL_popIndex()
    if(arg.lower() == "prall"):
        dictL_printAll()


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

