#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#get letter they want checked
letter = input("type a letter ")
#get sentence to be checked
sentence = input("type a sentence ")
#set variable before loop
count = 0
#start loop
for a in sentence:
  #check if variable is as same as letter
  if (a == letter):
    #add 1 to count
    count += 1
  else:
    #dont increase count
   count += 0
#display results
print("There are "  + str(count) + " " + str(letter) + "'s in " + str(sentence))

