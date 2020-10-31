import numpy as np
import matplotlib.pyplot as plt
 
''' Refresher '''
#Data types
def ints():
    num=2780 #assigning an integer to a variable
    print(num)
    num=-1625 #assigning a new variable
    print(num)

def floats():
    print (2.02975745) # A positive float
    print (-5.7289201) # A negative float
    flt_pt = 0.758391739
    print (flt_pt)

def complexbois():
    print(complex(10,20))
    complex_1=complex(0,2)
    complex_2=2+3j
    print(complex_1)
    print(complex_2)
    print("The real part of complex1 is: ",complex_1.real)
    print("The imaginary part of complex1 is: ",complex_1.imag)
    print("The real part of complex1 is: ",complex_2.real)
    print("The imaginary part of complex2 is: ",complex_2.imag)

def boolboi():
    print((True)," is ",int(True))
    f_bool=False
    print((f_bool), " is ", int(f_bool))

def stringbois():
    print("CATT")
    cat='cAt'
    print(cat)
    empty=""
    print(empty)

def morestrings():
    str1="Catherine"
    print(len(str1))
    first=str1[0]
    print(first)
    fourth=str1[3]
    print(fourth)
    last1=str1[8]
    print(last1)
    #or
    last2=str1[-1]
    print(last2)


#complexbois()  
#boolboi()  
#stringbois()
#morestrings()

#Operators
def Operators():
    x = 24
    y = 12
    z = 3
    print("x + y =", x + y )    # addition
    print("x - y =", x - y )    # subtraction
    print("y * z =", y * z )    # multiplication
    print("x / y =", x / y )    # division
    print("y**2 =", y**2 )      # exponential  
    print("x % 5 =", x % 5 )    # modulo
    print("x // 5 =", x // 5 )     # floor division

def PEMDAS():
    # Different precendence
    print ("10 - 3 * 2 =", 10 - 3 * 2) # Multiplication computed first, followed by subtraction
    # Same precedence
    print ("3 * 20 / 5 =", 3 * 20 / 5) # Multiplication computed first, followed by division
    # Using Parenthesis
    print ("(10 - 3) * 2 =", (10 - 3)  * 2) # subtraction computed first, followed by multiplication

def compare():
    x = 5
    y = 10
    z = 10
    print("y > x =",y > x) # 10 is greater than 5
    print("x > y =", x > y) # 5 is not greater than 10
    print("y is z =", y is z) # Both have the same value
    print("y is not x =", y is not x) # Both have different values
    print (3 + 10 == 5 + 5) # Both are not equal
    print (3 <= 2) # 3 is not less than or equal to 2

def logic():
    # OR Expression
    my_bool = True or False
    print (my_bool)
    # AND Expression
    my_bool = True and False
    print (my_bool) 
    # NOT expression
    my_bool = False
    print (not my_bool)

def ifsandbutts():
    num=10
    if num==10:
        print("The numba is 10")
    if num>10:
        print("numba greater than 10")
def ifelse():
    num=12
    if(num==10):
        print("The number is 10")
    else:
        print("The number is not 10")
#ifelse()

#loops
def forloopy():
    for i in range(1,11):
        if i%2==0:
            print(i, " is even")
        else:
            print(i, " is odd")

def loopdelist():
    int_list=[2,4,6,8,10]
    print(int_list)
    for i in range(0,len(int_list)):
        int_list[i]=int_list[i]**2
    print(int_list)

def iterate():
    int_list=[22,4,64,8,100]
    counter=0
    for num in int_list:
        if num>10:
            counter+=1
    print(counter)

def nested():
    num_list=[10,4,8,6,18,27,9]
    for n1 in num_list:
        for n2 in num_list:
            if(n1*2==n2):
                print(n1,n2)

def whilst():
    n=3
    power=0
    val=n
    while val <1000:
        power+=1
        val*=n
    print(power)

#forloopy()
#loopdelist()
#iterate()
#nested()
#whilst()

#functions
'''
def minimum (first, second):     # first and second are parameters
  if (first < second):   
    print (first)
  else:
    print (second)


#minimum (10, 20)    # num1 and num2 are arguments

def add(num1, num2, num3, num4=4, num5=5):   # num4 and num5 are optional
  return num1 + num2 + num3 + num4 + num5

#print(add(1, 2, 3))   # specifying values of num1, num2 and num3
#print(add(1, 2, 3, -4))   # specifying values of num1, num2, num3 and num4
#print(add(1, 2, 3, -4, -5))   # specifying values of num1, num2, num3, num4 and num5

def minimum (first, second):
  if (first < second):
    return first
  else:
    return second


result = minimum (10, 20) # Storing the value returned by the function
print (result)

num_list = [10, 20, 30, 40]
print (num_list)

def multiply_by_10(myList):
    for i in range(len(myList)):
        num_list[i] *= 10

multiply_by_10(num_list)
print (num_list) # The contents of the list have been changed

num = 20

def multiply_by_10(n):
    n *= 10             # Changing the value inside the function
    return n

multiply_by_10(num)
print (num)             # The original value remains unchanged
'''
# lambdas
square = lambda num: num ** 2 # Assigning the lambda to a variable
print (square(10)) # Calling the lambda and giving it a parameter

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print (concat_strings("Quantum", "Information", "Science"))

def calculator (operation, n1, n2):
  return operation(n1, n2) # Using the 'operation' argument as a function

# 10 and 20 are the arguments.
# The lambda multiplies them.
result = calculator(lambda n1, n2: n1 * n2, 10, 20) 

print (result)

# 10 and 20 are the arguments.
# The lambda adds them.
print (calculator(lambda n1, n2: n1 + n2, 10, 20))

# 10 and 3 are the arguments.
# The lambda computes 10^3
print (calculator(lambda n1, n2: n1 ** n2, 10, 3))



#lists
science = ["Physics", "Chemistry", 30]
print (science)

# Indexing is done using square brackets
print (science[0])

# Length
print (len(science))

science = ["Physics", "Chemistry", 30]
print (science)

# Indexing is done using square brackets
print (science[0])

# Length
print (len(science))

def merge1():
    part_A = [1, 2, 3, 4, 5]
    part_B = [6, 7, 8, 9, 10]
    merged_list = part_A + part_B
    print (merged_list)

def merge2():
    part_A2 = [1, 2, 3, 4, 5]
    part_B2 = [6, 7, 8, 9, 10]
    part_A2.extend(part_B2)
    print (part_A2)

lst = [1, 3, 5]
print(lst)

# print after append
print("List after append:")
lst.append(7)
print(lst)

#no comprehension
def no_comp():
    nums = [1, 2, 3, 4, 5]
    nums_square = []
    for n in nums:
        nums_square.append(n ** 2)
    print (nums)
    print (nums_square)


def comp():
    nums = [1, 2, 3, 4, 5]
    # List comprehension
    nums_square = [n**2 for n in nums]
    print (nums)
    print (nums_square)

def nested_nocomp():
    M = [[], [], [], [], []]
    for m in range(5):
        for n in range(5): 
            M[m].append(n + m * 20)
    print(M)

def nest_comp():
    M2 = [[(n + m * 20) for n in range(5)] for m in range(5)]
    print(M2)


#tuples and dictionaries

def tup():
    car = ("Ford", "Raptor", 2019, "Red")
    print (car)
    # Length
    print (len(car))
    # Indexing is done using square brakcers
    print (car[1])

def tup1add():
    hero1 = ("Superman", "Clark Kent")
    hero2 = ("Aquaman", "Arthur Curry")
    awesome_team = (hero1, hero2)
    print (awesome_team)

def tup2add():
    hero1 = ("Superman", "Clark Kent")
    hero2 = ("Aquaman", "Arthur Curry")
    awesome_team = hero1 + hero2
    print (awesome_team)


#dictionaries
def dict_stuff():
    empty_dict = {} # Empty dictionary
    print (empty_dict)

    phone_book = {"Batman": 428426, 
                "Superman": 28918398, 
                "Flash": 8198318}
    print (phone_book)
    print (phone_book["Batman"])
    print (phone_book.get("Flash"))
    print (phone_book)
    phone_book["Batman"] = 4209211 
    print (phone_book)

    if "Batman" in phone_book:
        print ("Gotham is saved.")
    else:
        print ("Gotham is in danger.")

    if "Aquaman" in phone_book:
        print ("Atlantis is saved.")
    else:
        print ("Atlantis is in danger.")   