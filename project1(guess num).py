import random

def rep_random():
  
  my=random.randint(1,10)
  return my

a=rep_random()
for i in range (1,10):
  i=int(input("num?"))
  if (i==a):
    print("r")
    break
  elif(i<a):
    print("low")
  else :
    print("far")
  
 
