#!/usr/bin/env python
# coding: utf-8

# In[ ]:


letter = input("type a letter ")
sentence = input("type a sentence ")

count = 0

for a in sentence:
  if (a == letter):
    count += 1
  else:
   count += 0

print("There are "  + str(count) + " " + letter + "s in " + sentence)

