import numpy as np


#vectors
def meth1():
	x = np.array([1, 3, 5, 7, 9])
	print(x)

def meth2():
	v1 = np.ones(5) # 5 ones
	v0 = np.zeros(5) # 5 zeros
	print(v1)
	print(v0)

def meth3():
	print(np.arange(1, 7))      # Takes default steps of 1 and doesn't include 7
	print(np.arange(5))     # Starts at 0 by defualt and ends at 4, giving 5 numbers
	print(np.arange(1, 10, 3))   

def meth4():
	print(np.linspace(1, 12, 12)) 
	print(np.linspace(1, 12, 5))
	print(np.linspace(1, 12, 3))

# meth1()
# meth2()
# meth3()
# meth4()

#Multidimensional Arrays

def multi1():
	x = np.ones((3, 4)) # An array with 3 rows and 4 columns of ones
	print(x)

def manual():
	x = np.array([[4, 2, 3, 2],
              	[2, 4, 3, 1],
              	[0, 4, 1, 3]])
	print(x)

def meshitup():
	x = np.arange(0, 5)
	y = np.arange(5, 11)
	[X, Y] = np.meshgrid(x, y)
	print("X is: \n",X) 
	print("Y is: \n",Y)

def shapeitup():
	x = np.array([[4, 2, 3, 2],
              [2, 4, 3, 1],
              [0, 4, 1, 3]])
	print(x)
	print()
	print(np.reshape(x, (2, 6)))  # 2 rows, 6 columns
	print()
	print(np.reshape(x, (1, 12)))  # 1 row, 12 columns

def properties1():
	v = np.array([1, 5, 9])
	M = np.array([[4, 2, 3, 2],
              [2, 4, 3, 1],
              [0, 4, 1, 3]])
	print("size of v is ", v.size)
	print("shape of v is ", v.shape)
	print("size of M is ", M.size)
	print("shape of M is ", M.shape)

def properties2():
	M = np.array([[4, 2, 3, 2],
              [2, 4, 3, 1],
              [0, 4, 1, 3]])
	print("Bytes per element of M is", M.itemsize)
	print("Number of bytes of M are", M.nbytes)
	print("Dimensions of M are", M.ndim)
	print("Data type of elements in M is", M.dtype)


#multi1()
#manual()
#meshitup()
#shapeitup()
#properties1()
#properties2()


#Indexing Arrays

def ind1():
	v = np.array([1, 5, 9])
	print(v[1])

def ind2():
	M = np.array([[4, 2, 3, 2],
              	[2, 4, 3, 1],
              	[0, 4, 1, 3]])
	print(M[1,2])	

def ind3():
	M = np.array([[4, 2, 3, 2],
              [2, 4, 3, 1],
              [0, 4, 1, 3]])
	print(M[1])

def ind4():
	M = np.array([[4, 2, 3, 2],
              [2, 4, 3, 1],
              [0, 4, 1, 3]])
	print(M[1,:]) # prints the entire 2nd row
	print(M[:,1]) # prints the entire 2nd column

def change():
	M = np.array([[4, 2, 3, 2],
              [2, 4, 3, 1],
              [0, 4, 1, 3]])
	print(M)
	M[2, 3] = 24 #changing element at 2nd row and 3rd column
	print("--------")
	print(M)

def slice():
	v = np.array([1, 3, 5, 7, 9, 11])
	print(v[2:4]) # 4th element will not be included

def moslice(): #array[lower:upper:step]
	v = np.array([1, 3, 5, 7, 9, 11])
	print(v[2::])
	print(v[:2:])
	print(v[::2])

def slicematrix():
	M = np.array([[(n + m * 20) for n in range(5)] for m in range(5)])
	print(M)
	print("------")
	print(M[1:4, 1:3]) # slice rows 1, 2 and 3 and columns 1 and 2 
#ind1()
#ind2()
#ind3()
#ind4()
#change()
#slice()
#moslice()
#slicematrix()


#ARRAY OPERATIONS

def ops1():
	v = np.arange(1, 11)
	print(v) 
	print("-----")
	print("Using scalar addition")
	print(v + 2) # adding 2 to each element in the vector
	print("-----")
	print("Using scalar subtraction")
	print(v - 2) # subtracting 2 from each element in the vector
	print("-----")
	print("Using scalar multiplication")
	print(v * 2) # multiplying each element by 2 in the vector
	print("-----")
	print("Using scalar division")
	print(v / 2) # dividing each element by 2 in the vector

def ops2():
	M = np.array([[(n + m * 20) for n in range(5)] for m in range(5)])
	print(M) 
	print("-----")
	print("Using scalar addition")
	print(M + 2) # adding 2 to each element in the matrix
	print("-----")
	print("Using scalar subtraction")
	print(M - 2) # subtracting 2 from each element in the matrix
	print("-----")
	print("Using scalar multiplication")
	print(M * 2) # multiplying each element by 2 in the matrix
	print("-----")
	print("Using scalar division")
	print(M / 2) # dividing each element by 2 in the matrix

def opsmatrix():
	M = np.array([[(n + m * 5) for n in range(3)] for m in range(3)])
	print("M")
	print(M) 
	N = np.array([[(n * 5) for n in range(3)] for m in range(3)])
	print("N")
	print(N) 
	print("-----")
	print("M * M")
	print(M * M) # multiplication
	print("-----")
	print("M + M") # addition
	print(M + M)
	print("-----")
	print("M - N") # subtraction
	print(M - N)
	print("-----")
	print("(M + 1) / (N + 1)")
	print((M + 1) / (N + 2)) # division 
	                         # to avoid division by zero, we have added scalar 1

def moreops():
	M = np.array([[(n + m * 5) for n in range(4)] for m in range(5)])
	print("M")
	print(M)        # 5 rows and 4 columns
	N = np.array([1, 2, 3, 4])
	print("N")
	print(N)        # 1 row and 4 columns
	print("-----")
	print("N * M")
	print(N * M)

def evenmore():
	M = np.array([[(n + m * 5) for n in range(4)] for m in range(5)])
	print("M")
	print(M) 
	N = np.array([[1], [2], [3], [4], [5]])
	print("N")
	print(N)
	print("-----")
	print("N * M")
	print(N * M)

#ops1()
#ops2()
#opsmatrix()
#moreops()
#evenmore()


#DATA PROCESSING

def stats():
	current = np.array([2.2, 2.5, 2.5, 2.7, 2.1, 2.5, 2.6, 2.5, 3.0, 2.9, 2.3, 2.8])
	print("mean", np.mean(current))     # to calculate mean
	print("standard deviation", np.std(current))    # to calculate standard deviation
	print("variance", np.var(current))      # to calculate variance
	print("maximum value:", np.max(current))     # to calculate maximum value
	print("minimum value:", np.min(current))     # to calculate minimum value

def complexboiss():
	arr = np.array([1+3j, 2+5j, 3+1j, 8-2j])
	print("Real part of arr =", arr.real)
	print("Imaginary part of arr = ", arr.imag)

def statops():
	v = np.arange(1, 10)
	print("Sum:", np.sum(v))
	print("Product:", np.prod(v))
	print("Cumulative Sum:", np.cumsum(v))
	print("Cumulative Product:", np.cumprod(v))

#stats()
#complexboiss()
#statops()


#SMART ARRAY PROGRAMMING

def cond():
	a = np.arange(10)
	print('the total array:', a)
	print("array of booleans:", a < 5)
	print('values less than 5:', a[a < 5])

def changeit():
	a = np.arange(10)
	print(a)
	a[a < 5] = 42
	print(a)

def multand():
	a = np.arange(20)
	print(a)
	a[(a > 5) & (a < 10)] = 42
	print(a)

def multor():
	a = np.arange(20)
	print(a)
	a[(a > 5) | (a < 10)] = 42 # everything changes
	print(a)

def anyall():
	v = np.linspace(-5, 5, 5)
	print(v)

	if (v > 0).any():
	  print("At least one element is positive.")
	else:
	   print("No element is positive.") 

	if (v > 0).all():
	  print("All elements are postive.")
	else:
	   print("Not all elements are positive.") 

def iterate():
	v = np.array([1, 2, 3, 4])
	for x in v:
  		print(x)

def iteratemulti():
	M = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
	for x in M:
	  for y in x:
	    print(y)
#cond()
#changeit()
#multand()
#multor()
#anyall()
#iterate()
#iteratemulti()

'''
def is_negative(x):
  if x < 0:
    return True
  else:
    return False
  
v = np.linspace(-5, 5, 5)
print(is_negative(v)) # this will throw an error
'''
#instead we do this!

def is_negative(x):
  if x < 0:
    return True
  else:
    return False

vec_is_negative = np.vectorize(is_negative) #vectorizing the function isNegative 
v = np.linspace(-5, 5, 5)
#print(v)
#print(vec_is_negative(v))

def copy1():
	a = np.arange(6)
	print("a =", a)
	b = a           # a is passed by reference and b is referring to same data as a
	print("b =", b)
	b[3] = 42      # changing in b will also change the value in a

	print("After replacing value in b")
	print("a =", a) # value is replaced in a as well
	print("b =", b)

def copy2():
	a = np.arange(6)
	print("a =", a)
	b = np.copy(a)       # a is copied in b
	print("b =", b)
	b[3] = 42      # changing in b will not change a

	print("After replacing value in b")
	print("a =", a) 
	print("b =", b)

# copy1()
# copy2()

#EXCERCISES:
#ex 1: get elements of 2- dim arrays
def ex1():
	arr = np.array([[4, 2, 3, 2], [2, 4, 3, 1], [2, 4, 1, 3], [4, 1, 2, 3]])
	print(arr)
	print('the first row of arr')
	print(arr[0])
	print('the first column of arr')
	print(arr[:, 0])
	print('the third row of arr')
	print(arr[2])
	print('the last two columns of arr')
	print(arr[:, -2:])
	print('the four values in the upper right hand corner')
	print(arr[:2, 2:])
	print('the four values at the center of arr')
	print(arr[1:3, 1:3])

#ex1()

#ex2: using conditions on arrays
def ex2():
	x = np.linspace(0, 2 * np.pi, 20)
	y = np.sin(x)
	arr1 = y[(y > 0.7) | (y < -0.5)]
	arr2 = y[(y > -0.5) & (y < 0.7)]
	print(arr1)
	print('-----')
	print(arr2)

#ex2()