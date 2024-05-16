string=input("enter the string to validate ")

i=0
state=0

while i<len(string):
  if state==0:
    if string[i]=='a':
      state=1
      i+=1
    elif string[i]=='b':
      state=3
      i+=1

  elif state==1:
    if string[i]=='a':
      state=1
      i+=1
    elif string[i]=='b':
      state=2
      i+=1
      
  elif state==2:
    if string[i]=='a':
      state=3
      i+=1
    elif string[i]=='b':
      state=2
      i+=1
  else:
    break  
if state==2:
    print(string,"string is accepeted",sep=" ")   
else:
    print(string,"NOT Accepted",sep=" ")     

