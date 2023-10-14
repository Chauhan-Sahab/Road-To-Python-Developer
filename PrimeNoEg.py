'''
Create a program to show the number is prime or not
'''

num =4
for i in range(2,num):
    if(num%i==0):
        print("Not a rpint")
        break;
else:
    print("It is prime")