#arithmetic operator 
a=10
b=4
print("addition",a+b)
print("subtraction",a-b)
print("multiplictaion",a*b)
print("division",a/b)
print("floor_division",a//b)
print("modulus",a%b)
print("expo",a**b)

#comparison operator 
a=5
b=10
print("equal=",a==b)
print("not equal=",a!=b)
print("less than =",a<b)
print("greater than =",a>b)
print("less than or equal to =",a<=b)
print("greater than or equal to =",a>=b)

#logical operator 
x=1 #true
y=0 #false
print("and operator",x and y)
print("or operator",x or y)
print("not operator",not x)
print("not operator",not y)

#assignment operator 
a=5
b=5
c=5
a+=5
b-=5
c*=5
print(a)
print(b)
print(c)

#membership operators
list=[1,2,3,4,5,6]
memb_in=3 in list
print(memb_in)
member_notin=8 in list 
print(member_notin)

name ="sagar"
memb_in="a" in name
print(memb_in)
member_notin="z" in name
print(member_notin)