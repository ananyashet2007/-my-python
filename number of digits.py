num = int(input("Enter an integer: "))
count = 0
n = abs(num)
if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print("Number of digits:", count)
output-
Enter an integer:  -1
Number of digits: 1
