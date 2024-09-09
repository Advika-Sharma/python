#list 
#oredered collection of items 
#list can contain different data types including integers, float, strings
#use []
#index based
#list are mutable(we can modify the data)
#allow duplication

#list=[1,1,2.0,3,4,5,"Data"]
#print(list)

list1=["hello","how","are","you"]
print(list1)
print(list1[1])
print(list1[-1])

#slicing
print(list1[:2])
#modify 
list1.append('?')
print(list1)
list1.remove('hello')
print(list1)
list1[0]='Banana'
print(list1)
list1[3]='Banana'
print(list1)

for i in list1:
    print(i)
    
#set 
#-----------------------
#unoredred collection of items 
#unique values(does not contain duplicates)
#use {}
#mutable
#automatically remove the duplicates 
#index


myset={1,2,3,4,5}
print(myset)
myset={1,2,3,4,5.0}
print(myset)
myset={1,2,3,4,4,5}
print(myset)
myset.add(6)
print(myset)
myset.remove(4)
print(myset)
name={'python','java','html'}
print(name)

print(2 in myset)
print(7 in myset)
print(7 not in myset)
for i in myset:
    print(i)
    
squarenum={i**2 for i in myset}
print(squarenum)

#Tuples
#---------------
#-ordered collection of elements, similar to list 
#it can contain different data types including integers, float, strings
#-immutable -> can not modify data (contents can not be changed after creation)
#-()
#allow duplication
#index based 

num=(10,10,20,30,20.65,'sagar')
print(num)
print(num[0])
print(num[-1])
print(num[2:4])
print(type(num))

#tuple unpacking
person=('sachin','kumar')
first_name,last_name=person
print(first_name)
print(last_name)

#iterating over tuples 
for i in num:
    print(i)
    
#-------------------------------------------------- 
#dictionary(dict)
#unordered collection of key-value pair (ex: set)
#key is unique and value can be duplicated 
#mutable
#{}, each data seperated by comma ,

my_dict={'a':10,'b':20,'c':30,'d':30}
print(type(my_dict))
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict['b'])
my_dict['b']=100
print(my_dict['b'])

for i in my_dict:
    print(i)
    print("----------------------------")
for i in my_dict.values():
    print(i)
print("----------------------------")

for char,val in my_dict.items():
    print(char,val)
print("-------------------------------")

print('a' in my_dict)  
print('a' not in my_dict)
print("-------------------------------")

print(len(my_dict))


#remove duplicate elements 
#write a program to remove the duplicates 
#ip-10,20,30,40,50,50
#op-10,20,30,40,50

my_list = [10, 20, 30, 40, 50, 50]
my_set = set(my_list)
#print(my_list)
print(my_set)
unique_list2 = list(my_set)
print(unique_list2)

