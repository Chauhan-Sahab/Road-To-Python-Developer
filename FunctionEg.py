def greet():
    print("Hi Chauhan Sahab")
greet()

#Non parameterize function
def Add2Num():
    a=int(input("Enter First Num"))
    b=int(input("Enter Second Num"))
    print(a+b)

#Add2Num()

#parameterize function
def Multiply2Num(a,b):
    print(a*b)

Multiply2Num(3,3)


#Non parameterize function with value return
def Substract2Num():
    return 5-2
result= Substract2Num()
print(result)


#Return Two values

def Return2Values():
    return 5,5
result1,result2=Return2Values()
print(result1,result2)


'''
There are two type of arguments
Formal:
eg:
def sum(a,b) here a,b is a formal argument

Actual Argument:sum(2,2) now the 2,2 is a actual argument

Actual arguments have four types:
1.Positon:It is important to use proper position like name has string or age has int
  let suppose we dont now the position the we can use as eg given bellow
2.Keywords:It is that we are use for positoning
3.Default: I we want to set any variable default value to it then we use it
4.Variable length: In a case when developer dont know how much parameter dows it need then we use * before the argument
  So it will increase the parameter dynamically what the user want 
'''

#Eg Postion and keywords
def sum(name,age):
    print(name)
    print(age)

sum(name="Chauhan",age=24)

#Default
def SumNum(a,b=10):
    return a-b


print(SumNum(2))



#We can pass dynamic arguments
def SumAll(*a):
    c=0
    for i in a:
        c+=i
    print(c)


SumAll(2,2,2,22)

#We can also add min req for one arguments

def Sub(a,*b):
    c=a
    for i in b:
            c-=i
    print(c) 

Sub(2,2,2,2,2)

#KeyWorded lenght Argument

def UserData(name,**data):
    print(name)
    print(data)

UserData("Abhijeet",surname="Singh",lastname="Chauhan")

def NewUserData(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

NewUserData("Abhijeet",surname="Singh",lastname="Chauhan")



