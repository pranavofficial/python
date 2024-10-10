#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get letter they want checked
letter = input("type a letter ")
#get sentence to be checked
sentence = input("type a sentence ")
#set variable before loop
count = 0
#start loop
for a in sentence:
  #check if variable is as same as letter
  if (a.lower() == letter.lower()):
    #add 1 to count
    count += 1
  else:
    #dont increase count
   count += 0
#display results
print("There are "  + str(count) + " " + letter + "'s in " + sentence)


# In[5]:


# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

string1 = input('Type the sentence you want checked ')

# make it suitable for caseless comparisions
string1 = string1.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in string1:
   if char in count:
       count[char] += 1

print(count)


# In[ ]:




