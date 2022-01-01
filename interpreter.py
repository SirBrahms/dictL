import os
import re

#Defining global variables
arg = ""
paramList = []
pos = 1 #position/"index" in the main dictionary
pushvar = 0 #variable to store the position passed by pushI
ifpos = 1 #variable used to navigate the "ifdict" dictionary
operations = ["+", "-", "*", "/"]


#defining the starting dictionary
maindict = {}
#defining the dictionary to hold all arguments for "if" statements
ifdict = {}

#function to distinguish the first element in a line and seperate it
def formStrings(fulllist):
    global arg, paramList
    arg = fulllist[0]
    fulllist.remove(arg)
    paramList = fulllist

#function to convert lists into strings
def ListToString(listStr):
    retStr = ""
    for e in listStr:
        retStr += e + " "
    return retStr

def fillifDict():
    global lines, ifdict
    events = []
    eventsFull = []

    for line in lines:
        match = re.search(r">(.*)", line)
        if match:
            events.append(match.group(1))
    for command in events:
        stripcommand = command.strip()
        if(stripcommand == "!"):
            ifdict[str(len(ifdict)+1)] = eventsFull
            eventsFull = []
        else:
            eventsFull.append(stripcommand)
        
#dictL code functions commence here
def dictL_add():
    global paramList, maindict
    if(paramList == [] or paramList[0] == "nul"):
        maindict[str(len(maindict)+1)] = "nul"
        return
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
        if(paramList[0] != None and paramList[0] != len(maindict) and not "?lit" in paramList):
            print(maindict[str(paramList[0])])
            return
        elif("?lit" in paramList):
            for e in paramList:
                if(e != "?lit"):
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

def dictL_if(literacy = ""):
    global ifdict, paramList, lines, ifpos, maindict
    #params: [0] = operand 1 [1] = operator, [2]

    if(literacy == ""):
        if(str(paramList[0]) in maindict):
            paramList[0] = maindict[str(paramList[0])]
        if(str(paramList[2]) in maindict):
            paramList[2] = maindict[str(paramList[2])]

    if(paramList[1] == "=="):
        if(paramList[0] == paramList[2]):
            for e in ifdict[str(ifpos)]:
                fullsplitlist = e.split(" ")
                formStrings(fullsplitlist)
                if(arg in maindict):
                    checkArith(arg)
                else:
                    checkArg(arg)
        ifpos += 1
    elif(paramList[1] == "!="):
        if(paramList[0] != paramList[2]):
            for e in ifdict[str(ifpos)]:
                fullsplitlist = e.split(" ")
                formStrings(fullsplitlist)
                checkArg(arg)
                if(arg in maindict):
                    checkArith(arg)
                else:
                    checkArg(arg)
        ifpos += 1

def dictL_input(add = ""):
    global paramList, maindict
    fullstring = ""
    num = 0
    
    if(add == ""):
        if(paramList != []):
            try:
                for e in paramList:
                    if(num != 0):
                        fullstring += e + " "
                    num += 1
                maindict[str(paramList[0])] = input(fullstring)
            except:
                print("Error whilst generating input")
                exit()
    else:
        if(paramList != []):
            try:
                for e in paramList:
                    fullstring += e + " "
                maindict[str(len(maindict)+1)] = input(fullstring)
            except:
                print("Error whilst generating input")
                exit()

def checkArg(arg):
    global maindict, pos
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
    elif(arg.lower() == "if?"):
        dictL_if("True")
    elif(arg.lower() == "inp"):
        dictL_input()
    elif(arg.lower() == "inp+"):
        dictL_input("+")

def checkArith(arg):
    global operations, paramList, maindict
    listarg = [""] #initialisation of an empty list for listifying "arg" into
    #check if arg is = ""
    if(arg != ""):
        listarg = list(arg)
    
    if(paramList != [] and len(paramList) == 2 and arg != len(maindict)+1):
        if(paramList[0] in operations and arg[0]):
            try:
                if(paramList[0] == "+"):
                    maindict[str(arg)] = int(maindict[str(arg)]) + int(maindict[str(paramList[1])])
                elif(paramList[0] == "-"):
                    maindict[str(arg)] = int(maindict[str(arg)]) - int(maindict[str(paramList[1])])
                elif(paramList[0] == "*"):
                    maindict[str(arg)] = int(maindict[str(arg)]) * int(maindict[str(paramList[1])])
                elif(paramList[0] == "/"):
                    maindict[str(arg)] = int(maindict[str(arg)]) / int(maindict[str(paramList[1])])
            except:
                pass
        if(paramList[0] in operations and listarg[0] == "?"):
            listarg.remove("?")
            arg = ListToString(listarg)
            if(paramList[0] == "+"):
                maindict[str(arg)] = int(arg) + int(paramList[1])
            elif(paramList[0] == "-"):
                maindict[str(arg)] = int(arg) - int(paramList[1])
            elif(paramList[0] == "*"):
                maindict[str(arg)] = int(arg) * int(paramList[1])
            elif(paramList[0] == "/"):
                maindict[str(arg)] = int(arg) / int(paramList[1])


#opening the file
try:
    file1 = input("Enter file to open: ")
    openfile = open(file1, "r")
    lines = openfile.readlines()
except:
    print("The file", file1,"doesn't exist")
    exit()

fillifDict()

#format each line properly
for e in lines:
    stripstring = e.strip()
    splitstring = stripstring.split(" ")
    formStrings(splitstring)
    if(arg in maindict):
        checkArith(arg)
    else:
        checkArg(arg)

