 # sum until negative number 
total = 0
while True:
    number = int(input("Enter a number (negative number to stop): "))
    if number < 0:
        break
    total += number
print("The sum of entered numbers is:", total)
output-

Enter a number (negative number to stop):  -6
The sum of entered numbers is: 0

