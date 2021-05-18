#question 1
data=list(range(2000,3201))
output=[]
for i in data:
    if(i%7==0 and i%5!=0):
        output.append(i)
print(output)
#question 2
x=input("enter first name")
y=input("enter last name")
output=x+" "+y
out_new=output[::-1]
print(out_new)
#question 3
diameter=12
r=diameter/2
v=eval('(4/3)*3.14*(r**3)')
print(v)