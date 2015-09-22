#written may 1 2015
#Nikki Sigurdson
#takes in twitter txt data, cleans and returns text file of usernames
# and a seperate one of tweet raw data
from string import *
wtxt = open("cleaned_data.txt", 'w')
rtxt = open("TEXT_hockey__1430678626.txt", 'r')
wtxt2 = open("cleaned_data2.txt", 'w')
'''
note: these textfiles should be named with their seconds date format
filenames.
'''
listt = []
tempp = []
for line in rtxt:
     #seperate the string by a delimiter into parts of a list
     tempp = str(line).split(",")
     
     listt.append(tempp[0])
     try:
          tempp[0] = int(tempp[0])
          #note: use concatenation function to compress str data?
          wtxt.write(tempp[0])
          wtxt.write("\n")
     except:
          continue
     try:
          wtxt2.write(tempp[2] )
     except:
          continue
     
rtxt.close()
wtxt.close()
wtxt2.close()

#next to-do:
'''
- we need to find a way to get the program to parse through txt files with
different filenames. need to access the OS library to do that probably.
make a huge loop that will do that.

- need to collect the text data and do string analysis of it, for most
common words. DONE

- get rid of space in front of user names. get rid of all the
excess blanks everywhere.
'''
