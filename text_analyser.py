#text_analyser
#nikki sigurdson
#may 17 2015

import os

# purpose: takes in raw data from .txt file,
# creates dictionary of all strings DLM = " "
# along with a value which is str frequency.

# returns a dictionary type.

def text_analyser(txtfilename):
     idict = {}
     rtxt = open( txtfilename, 'r')
     for line in rtxt:
         splitline = line.split(" ")
         for string in splitline:
             if string not in idict:
                 idict[string] = 0
             else:
                 idict[string] += 1       
     rtxt.close()
     return idict


def list_creator(dictt):
    counter = 0
    temp1 = ""
    mylist = []
    
    tempdict = dictt
    print(dictt)
    # temp1 is the largest current value in dictt
    for m in range(0, len(dictt)):
      print(m, "-------------------------------------")
      for i in tempdict:
            if tempdict[i] > counter:
               temp1 = i
               counter = tempdict[i]
            # now we have the value of the next most freq string.
      mylist.append( temp1 )
    return mylist 

mydict2 = text_analyser("hockey_15.txt")
mydict = text_analyser("hockey_3.txt")

#takes a dictionary input
def printoutlist(mydict):
 mylist  = sorted(mydict.values())
 mylist2= sorted(mydict, key= mydict.__getitem__)
 for i in range(0 , len(mylist) ):
          print (mylist[i] , mylist2[i])



def text_analysis_package(txtname):
     dictt = text_analyser(txtname)
     printoutlist(dictt)
     print("length of dictionary: ", len(dictt))

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

clndata = ["cleannedhockey2.txt","cleannedhockey3.txt","cleannedhockey4.txt",
                 "cleannedhockey5.txt","cleannedhockey6.txt","cleannedhockey7.txt",
                 "cleannedhockey8.txt","cleannedhockey9.txt","cleannedhockey10.txt",
                 "cleannedhockey11.txt","cleannedhockey13.txt",
                 "cleannedhockey14.txt","cleannedhockey15.txt"]

mastdict = {}
for i in clndata:
     #dict of that txtfiles user ids
     tempdict = text_analyser(i) 

     #add it to the master dict
     mastdict = merge_two_dicts(tempdict, mastdict)

#printoutlist(mastdict)
print(len(mastdict))

















































