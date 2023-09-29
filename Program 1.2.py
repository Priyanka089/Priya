yea=int(input("enter tha year to be find"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("it is a leap year")
    else:
      print("it is not a leap year")
  else:
      print("it is a leap year ")
else:
  print("it is not a leap year ")
