from numpy import *
#from array import *
arr=[[2.0,2,2,2,2],[2,2,2,2,2]]
for i in arr:
    for j in i:
        print(j,end="")
    print()

'''
This is linspace in this we provide (start,stop , parts)

Start: It is starting point 
Stop : It is ending point. i.e included
Parts: It is the start and stop is break into that much part and
       if we didn't provode it then it will part it into 50 that is default
'''
arr1= linspace(0,15,17)
print(arr1)

'''
Arange: it will work like looop for creating the array
        it has start , stop and steps
'''

arr2=arange(0,20,2)
print("This is arange function")
print(arr2)


'''
Logspace: It will work same like linsspace buut the main difference is
          The gap between the two elements will be the same.
          although in linspace the cap is not same.
'''

arr3=logspace(0,15,6)
print("This is logspace")
print(arr3)
print('%.2f'%arr3[0])


'''
Zeros: If i want to create a array of all the zeros the we use zero
Ones: Same work as zeros but it will assign 1
'''

arr4=zeros(5)
print(arr4)
arr5=ones(5)
print(arr5)
arr6=ones(5,int)



 #Assignment add 5 to each element of array
addedArray=arr5+5
print(addedArray)



#Copying Array
'''
In this copy both the valriable have same address
'''
a1=addedArray

'''
We can copy array in two ways:
Shallow Copy
Deep Copy

In .View() it is copying in the shallow coppy 
lets suppose if we change in addedArray it will 
Change in a1 array as well

But in .Copy() this is it will not change
'''
#Shallow Copy
a1=addedArray.view()
print(addedArray)
addedArray[0]=33

print(a1)

#Deep Copy

a2=addedArray.copy()
addedArray[0]=88
print(addedArray)
print(a2)
#Find the address of the array or any variable
print(id(a2))


#We can also add two array using numpy

a3=a1+a2
print(a3)
