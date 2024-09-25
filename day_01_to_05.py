Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World
name="Shivam"
age=21
print("Name:",name,"Age:",age)
Name: Shivam Age: 21
x=5
y=7
print("x=",x,"y=",y,"sum=",x+y)
x= 5 y= 7 sum= 12
percentage=85.75
print("Score:{:2f}%".format(percentage))
Score:85.750000%
x=10
y=5
if x>y:
    print("x is greater than y")
    else
    
SyntaxError: invalid syntax
print("y is greater than or equal to x")
y is greater than or equal to x
x=10
y=5
if x>y:
    print("x is greater than y")
    else
    
SyntaxError: multiple statements found while compiling a single statement
x=10
y=5
if x>y:
    print("x is greater than y")
    else:
        
SyntaxError: multiple statements found while compiling a single statement
x=10
y=5
if x>y:
    print("x is greater than y")

    
SyntaxError: multiple statements found while compiling a single statement
x=10
y=5
if x>y:
    print("x is greater than y")

    
x is greater than y
x=10
y=5
if x>y:
    print("x is greater than y")
    
SyntaxError: multiple statements found while compiling a single statement
x=10
y=7
if x>y:
    print("x is greater than y")
    else:
        
SyntaxError: invalid syntax
x=10
y=7
if x>y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")

    
x is greater than y
fruits=["appple","banana","cherry"]
for x in fruits:
    print(x,end="")

    
appplebananacherry
fruits=["appple","banana","cherry"]
for x in fruits:
    print(x,end=" ")
    
SyntaxError: multiple statements found while compiling a single statement
i=1
while i<5:
    print(i,end=" ")
    i+=1

    
1 2 3 4 
fruits=['apple','banana','cherry']
print("fruits[1]=",fruits[1])
fruits[1]= banana
fruits.append('orange')
print("fruits="fruits)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
fruits.append('ornage')
print("fruits=",fruits)
fruits= ['apple', 'banana', 'cherry', 'orange', 'ornage']
num_list=[1,2,3,4,5]
sum_nums=sum(num_list)
>>> print("sum_nums=",sum_nums)
sum_nums= 15
>>> 
>>> 
>>> 
>>> 
>>> 
>>> point=(3,4)
>>> x,y=point
>>> print("(x,y)=",x,y)
(x,y)= 3 4
>>> tuple_=('apple','banana','cherry','orange')
>>> print("Tuple=",tuple_)
Tuple= ('apple', 'banana', 'cherry', 'orange')
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> set1={1,2,2,3,1,4}
>>> print("set1=",set)
set1= <class 'set'>
>>> print("set1=",set1)
set1= {1, 2, 3, 4}
>>> set2={'apple','cherry','orange','banana'}
>>> print("set2=",set2)
set2= {'apple', 'orange', 'banana', 'cherry'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> person={'name':'umesh','age':25,'city':noida}
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    person={'name':'umesh','age':25,'city':noida}
NameError: name 'noida' is not defined
>>> 
>>> 
>>> 
>>> person={'name':'umesh','age':25,'city':'noida'}
>>> print("person=",person)
person= {'name': 'umesh', 'age': 25, 'city': 'noida'}
>>> print(person['name'])
umesh
>>> 
>>> person['age']=27
>>> print("person=",person)
person= {'name': 'umesh', 'age': 27, 'city': 'noida'}
