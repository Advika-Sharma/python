#it will always allows you to execute a block of code repeatedly 
#useful for automating repetitive tasks, processing collection of data and iterating over a sequence 
#for loops
#used to iterate over a sequence (such as list, tuple, string, range) and 
#execute a block of code for reach time 
#-----------------------------------
print("Iterating over a list")
num=[1,2,3,4,5]
for i in num:
    print(i)
#           or

print("Iterating over a list")
num=[1,2,3,4,5]
for n in num:
    print(n)

#-----------------------------
print("Iterating over a string")
for char in "SAGAR":
    print(char)

#           or
print("Iterating over a string")
for name in "SAGAR":
    print(name)
    
#------------------------
print("Iterating over a range")
#range -> start point , ending point, a step/ gap in it 
#+1 is added to ending point whule defining a range 
for i in range (1,7):
    print(i)

for i in range(1,4):
    print("Hello World")
    
    
#creating multiplication table 
n=12
for i in range(1,11):
    #print(n*i)
    print(n,"x",i,"=",n*i)

#------------------------------
#break -> terminates the loop permananently 
num=[1,2,3,4,5]
for i in num:
    if i==4:
        break
    print(i)
    
    
    
#while loops 