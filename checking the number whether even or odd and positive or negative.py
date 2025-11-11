# program for even/odd and positive/negative
num=int(input("enter the num"))
if num>0:
  print("the num is positive")
elif num<0:
  print("the num is negative")
else:
  print("zero")

if num.is_integer():
    if num%2==0:
        print("even number")
    else:
        print("odd number")
output-
enter the num6
the num is positive
even number

