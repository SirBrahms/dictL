import os
import re

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

def ListToString(listStr):
    retStr = ""
    for e in listStr:
        retStr += e + " "
    return retStr

#dictL code functions commence here
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
    if(paramList != []):
        if(paramList[0] != None and paramList[0] != len(maindict) and not "!lit" in paramList):
            print(maindict[str(paramList[0])])
            return
        elif("!lit" in paramList):
            for e in paramList:
                if(e != "!lit"):
                    fullprint += e + " "
            print(fullprint)
            return
    if(maindict != {}):
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

def dictL_exit():
    exit()

def dictL_if():
    global paramList, lines
    events = []

    for line in lines:
        match = re.search(r"{(.+?)}", line)
        if match:
            events.append(match.group(1))
    print(events)

def checkArg(arg):
    global maindict
    global pos
    listarg = [""] #initialisation of an empty list for listifying "arg" into

    #check if arg is = "" (for proper comment-implementation)
    if(arg != ""):
        listarg = list(arg)

    if(arg == "*" or listarg[0] == "*"):
        return
    elif(arg.lower() == "add"):
        dictL_add()
    elif(arg.lower() == "up" and pos != len(maindict) and maindict != {}):
        dictL_up()
    elif(arg.lower() == "dw" and pos != 1 and maindict != {}):
        dictL_down()
    elif(arg.lower() == "prn"):
        dictL_print()
    elif(arg.lower() == "rst"):
        dictL_reset()
    elif(arg.lower() == "jti" and maindict != {}):
        dictL_jumpToIndex()
    elif(arg.lower() == "chng" and maindict != {}):
        dictL_change()
    elif(arg.lower() == "pushi" and maindict != {}):
        dictL_pushIndex()
    elif(arg.lower() == "popi" and maindict != {}):
        dictL_popIndex()
    elif(arg.lower() == "prall"):
        dictL_printAll()
    elif(arg.lower() == "exit"):
        dictL_exit()
    elif(arg == "" or arg == " "):
        return
    elif(arg.lower() == "if"):
        dictL_if()
    """
    else:
        print("Error whilst interpreting: ", arg , "is not a valid argument!")
        exit()
    """

#opening the file
try:
    file1 = input("Enter file to open: ")
    openfile = open(file1, "r")
    lines = openfile.readlines()
except:
    print("This file doesn't exist")
    exit()

#format each line properly
for e in lines:
    stripstring = e.strip()
    splitstring = stripstring.split(" ")
    formStrings(splitstring)
    checkArg(arg)

