Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={"mon","tue","wed"}
type(s)
<class 'set'>
s(1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s(1)
TypeError: 'set' object is not callable
s{1}
SyntaxError: invalid syntax
s[1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s.add("thru")
s
{'tue', 'wed', 'mon', 'thru'}
s={"mon","tue","wed"}
type(s)
<class 'set'>
s(1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s(1)
TypeError: 'set' object is not callable
s{1}
SyntaxError: invalid syntax
s[1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s.add("thru")
s
{'tue', 'wed', 'mon', 'thru'}
SyntaxError: multiple statements found while compiling a single statement
s.discard("tue")
s
{'wed', 'mon', 'thru'}
s.remove("tue")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.remove("tue")
KeyError: 'tue'
D=(101:'ce',102:'me',105:'cse')
SyntaxError: invalid syntax

D=(101:"ce",102:"me",105:"cse")
SyntaxError: invalid syntax
D={101:"ce",102:"me",105:"cse"}
D
{101: 'ce', 102: 'me', 105: 'cse'}
D.keys()
dict_keys([101, 102, 105])
D.values()
dict_values(['ce', 'me', 'cse'])
D(105)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    D(105)
TypeError: 'dict' object is not callable
D{105}
SyntaxError: invalid syntax
D[105]
'cse'
D[105]="cse(IOT)"
D
{101: 'ce', 102: 'me', 105: 'cse(IOT)'}
D.update({105:["cse","cse(IOT)"]})
D
{101: 'ce', 102: 'me', 105: ['cse', 'cse(IOT)']}
class car:
    def_int_(self)
    self.brand="suruki"
    self.color="blue"
    self.top_speed=200

    
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    class car:
  File "<pyshell#30>", line 2, in car
    def_int_(self)
NameError: name 'def_int_' is not defined
class car:
    def_int_(self):
    self.brand="suruki"
    self.color="blue"
    self.top_speed=200
    
SyntaxError: invalid syntax

class car:
    def__int__(self):
    self.brand="suruki"
    self.color="blue"
    self.top_speed=200
    
SyntaxError: invalid syntax
class car;
    def_int_(self):
        self.brand="suruki"
        self.color="blue"
        self.top_speed=200
        
SyntaxError: invalid syntax
class car:
    def_init_(self):
    self.brand="suruki"
    self.color="blue"
    self.top_speed=200
    
SyntaxError: invalid syntax
class car:
    def _init_(self):
        self.brand="suzuki"
        self.color="blue"
        self.top_speed=200

        

car=car()
car.brand
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    car.brand
AttributeError: 'car' object has no attribute 'brand'
car.color
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    car.color
AttributeError: 'car' object has no attribute 'color'
car.color
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    car.color
AttributeError: 'car' object has no attribute 'color'
class car:
    def _init_(self):
        self.brand="suzuki"
        self.color="blue"
        self.top_speed=200

        
car=car()
car.brand
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    car.brand
AttributeError: 'car' object has no attribute 'brand'
class car:
    def __init__(self):
        self.brand="suzuki"
        self.color="blue"
...         self.top_speed=200
... 
...         
>>> car=car()
>>> car.brand
'suzuki'
>>> car.color
'blue'
>>> car.top_speed
200
>>> class car:
...     def __init__(self,b,c,ts):
...         self.brand=b
...         self.color=c
...         self.top_speed=ts
...         def accelerate(self):
...             print("your car top speed is :",self.top_speed)
... 
...             
>>> car=car("tata","gray",255)
>>> car.accelerate()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    car.accelerate()
AttributeError: 'car' object has no attribute 'accelerate'
>>> 
>>> 
>>> class car:
...     def __init__(self,b,c,ts):
...         self.brand=b
...         self.color=c
...         self.top_speed=ts
...     def accelerate(self):
...             print("your car top speed is :",self.top_speed)
... 
...             
>>> car=car("tata","gray",255)
>>> car.accelerate()
your car top speed is : 255
