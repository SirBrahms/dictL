import os

#Defining global variables
arg = ""
paramList = []

#test124567

#function to distinguish the first element in a line and seperate it
def formStrings(fulllist):
    global arg
    global paramList
    arg = fulllist[0]
    fulllist.remove(arg)
    paramList = fulllist

#opening the file
file1 = input("Enter file to open: ")
openfile = open(file1, "r")
lines = openfile.readlines()

#format each line properly
for e in lines:
    stripstring = e.strip()
    splitstring = stripstring.split(" ")
    formStrings(splitstring)
    print(arg)
    print(paramList)
