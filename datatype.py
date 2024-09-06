#list 
#oredered collection of items 
#list can contain different data types including integers, float, strings
#use []
#index based
#list are mutable(we can modify the data)
#allow duplication

list=[1,1,2.0,3,4,5,"Data"]
print(list)

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