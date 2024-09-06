print("hello world")
#print("hello students\n welcome to data analytics course")
print("""
      hello students
      welcome to 
      data analytics course
      """)
print('''
      hello students
      welcome to 
      data analytics course
      ''') #this is multiline content 
#variable->container used to store data 
a = 10
b =  20.6
print(type(a))
print(type(b))
print(a,b)
name = "sagar"
print(type(name))
print(name)
#rules
#1. numbers and special keywords not allowed 
#2. spaces not allowed while creating variables, can use _ underscore 
#-----------------------------------

a,b,c=10,20,30
print(a,b,c)  
#----------------------
a=b=c=10
print(a,b,c)

#data types
#user-inputs
name=input("enter your name")
print("my name is ",name)

#-------------------------------
age=int(input("enter your age"))
print("my age is",age)

#type casting
num=30
marks=25.7
print(type(num))
print(type(marks))
result=marks - num
print(type(result))

a="123"
print(type(a))

a=int(a)
print(type(a))

#write a program to add 2 numbers 
a=10
b=20
c=a+b
print(c)