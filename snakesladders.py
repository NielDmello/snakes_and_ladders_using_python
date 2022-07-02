import random
a = 1
b = 1
while a < 100 and b < 100:
  d = [1, 2, 3, 4, 5, 6]  
  rad=int(input("press 1 for rollind the dice for a:"))
  if rad==1:
     dice=random.choice(d)
     print("value of dice is :",dice)
  else:
     print("dicenot rolles")
  a=a+dice
  print("A is now on :",a)
  
  thisdict = {
  "2":23,
  "6": 45,
  "20": 59,
  "43": 17,
  "50": 5,
  "52": 72,
  "56": 8,
  "57": 96,
  "71": 92,
  "73": 15,
  "84": 58,
  "87": 49,
  "98": 40
   }
  if str(a) in thisdict:
     a=int(a)
     y=thisdict[str(a)]
     if a<y:
        a=y
        print("Hurray! Got a ladder new value is ",a)
     else:
        a=y
        print("Oops! Got a Snake new value is ",a)
  else:
     print(a)

  rbd=int(input("press 1 for rollind the dice for b:"))
  if rad==1:
     diceb=random.choice(d)
     print("value of dice is :",diceb)
  else:
     print("dicenot rolles")
  b=b+diceb
  print("B is now on :",b)

  if str(b) in thisdict:
     b=int(b)
     y=thisdict[str(b)]
     if b<y:
        b=y
        print("Hurray! Got a ladder new value is ",b)
     else:
        b=y
        print("Oops! Got a Snake new value is ",b)
  else:
     print(b)

     
if a>b:
  print("A is winner")
else:
  print("B is winner")