import random

num = random.randint(1, 10)


g1 = int(input("Guess the number I randomly picked between 1 and 10. You have 3 tries. "))

if (g1 > num):
  print ("Too High")
elif (g1 < num):
  print ("Too Low")
else:
  print ("Wow, are you hacking? Because that was correct.")
  quit()
  

g2 = int(input("Guess Again "))

if (g2 > num):
  print ("Too High")
elif (g2 < num):
  print ("Too Low")
else:
  print ("Wow, are you hacking? Because that was correct.")
  quit()

g3 = int(input("Guess Again "))

if (g3 > num):
  print ("You lose")
  quit()
elif (g3 < num):
  print ("You lose")
else:
  print ("Wow, are you hacking? Because that was correct.")
  quit()