
#num=int(input("enter a number"))

factorial=1

#check if the number is negative, positive or zero
if num<0:
  print("sorry, factorial does not exist for negative number")
elif num==0:
  print("factorial of 0 is 1")
else:
  for i in range(1,num+1):
    factorial=factorial*i
  print("the factorial of",num,"is"factorial)
