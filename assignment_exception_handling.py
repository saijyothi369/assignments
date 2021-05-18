#Question 1
try:
    print (5/0)
except ZeroDivisionError as e:
    print("Division by zero is not allowed")

#Question 2
subject=["Americans","Indians"]
verb=["play","watch"]
objects=["Baseball","cricket"]
for i in subject:
    for j in verb:
        for k in objects:
            print(i,j,k)