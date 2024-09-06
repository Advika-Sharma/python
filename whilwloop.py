print("while loop")
count=0
while count<5:
    print(count)
    count +=1
    
#break -> terminates the loop
print("break condition")
list=[1,2,3,4,5,6,7,8,9]
for num in list:
    if num==5:
        break
    print(num)
    
    
#continue -> skips the current iteration and procedes to the next iteration of the loop
print("continue condition")
list=[1,2,3,4,5,6,7,8,9]
for num in list:
    if num == 5:
        continue
    print(num)
    
#pass -> acts as a placeholder, there will be no action
for i in range(5):
    pass

    
