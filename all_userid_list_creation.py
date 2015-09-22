#nikki sigurdson may 10 2015
#all_userid_list.py
#makes the master list of all userid's for use in the
#interconnectedness analysis of the hockey tweeters.

from twitter_setup import api

'''
method:
parse through all the (SAS-precleaned) text file datasets.
creates a master list of all the collected userids.

'''
from make_list import *

filename = "cleannedhockey15.txt"
mylist = make_list( filename )


#first, right now, lets check to see if mylist has any duplicates.

master = []
for user in mylist:
    #print ("USERNAME:" , user )
    if user not in master:
        master.append(user)
    else:
        None
       # print("duplicate detected. ---" , user )

'''

mylist is a list of all tweets ID's in the file - including duplicates.
master is a list of just pure unique ID's. 
'''



    

'''
- accept all usernames into a var
- have a dictionary to collect the names and value is freq
- at the end print the sorted dictionary

total users is the length of the dictionary. 

'''
'''

clndata = ["cleannedhockey2.txt","cleannedhockey3.txt","cleannedhockey4.txt",
                 "cleannedhockey5.txt","cleannedhockey6.txt","cleannedhockey7.txt",
                 "cleannedhockey8.txt","cleannedhockey9.txt","cleannedhockey10.txt",
                 "cleannedhockey11.txt","cleannedhockey13.txt",
                 "cleannedhockey14.txt","cleannedhockey15.txt"]
userdict = {}

for i in range ( 0 , len(clndata)):
     userids = make_list(clndata[i])
     for userid in userids:
          if userid not in userdict:
               userdict[userid] = 1
          else:
               userdict[userid] += 1


userdict2  = sorted(userdict.values())


#finding the most frequent user id's in the dict
def printfrequsers():
    number = 0
    useridtemp = ""
    usedlist = []
    att = 0
    for i in range(0,100): # we want top 5 users
     print( att , "\n")
     att+=1
     #try:
     for userid in userdict:
            #if userdict[userid] > number:
                   # number = userdict[userid]
                    useridtemp = userid
                    #usedlist.append(userid)
                    print(useridtemp, number)
                    mm = api.users.lookup(user_id = str(useridtemp) )
                    print (mm[0]['screen_name'] , mm[0]['name'])
                        
     #except:
     #    print("exception occurred. \n")
       #  None





'''






















    



