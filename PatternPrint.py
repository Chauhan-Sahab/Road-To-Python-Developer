'''
Question 1 

print this:

####
####
####
####



Question 2
print this:

*
**
***
****
*****
'''


# for i in range(0,3):
#     print('*',end="")
#     for j in range(0,3):
#         print('*',end="")
#     print()


# for i in range(0,4):
#     print("*",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

num = 4
for i in range(4):
    num-=1
    print('#',end="")
    for j in range(4-i):
        print("#",end="")
    print()
