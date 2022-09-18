# Write a python script to print first N even natural numbers in reverse order
n = int(input("enter value of n "))
i = 2*n
while i > 1:
    print(i)
    i -= 2
