list1=[3,4,487,48,485,25,356,354,51,52,1,2284,22641,22]
templist=[]
for i in list1:
    if(i%2==0):
        templist.append(i)
print(templist)
list2=[i for i in list1 if i%2==0]
print(list2)