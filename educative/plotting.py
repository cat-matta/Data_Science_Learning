import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D



#help("matplotlib.pyplot.plot") #for help
#basic plotting
def plot1():
	x = np.linspace(0, 2, 100)
	y = x ** 2
	fig = plt.figure(figsize=(10, 5), dpi=100)
	ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])      #add_axes([bottom x, bottom y, width, height])
	ax1.plot(x, y, 'bo')
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.set_title('Example figure')
	plt.show()

def plot2():
	x = np.linspace(0, 2 *np.pi , 100)
	y = np.sin(x)
	fig = plt.figure(figsize = (10, 5))
	ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	ax1.plot(x, y, color='g', marker='o', linestyle='-', linewidth=4, markersize=15)
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.set_title('y = sin(x)')
	plt.show()


def plot3():
	x = np.linspace(0, 2, 100)
	y = x ** 2
	fig = plt.figure(figsize=(10, 5))
	ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	ax1.plot(x, y, 'b')
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.set_title('Example figure')
	plt.show()


#fig.savefig('output/out.png') # saving in the output directory to save
# plot1()
#plot2()
# plot3()

#multiple plots!!!
def multiple1():
	x = np.linspace(0, 2 * np.pi , 100)
	y1 = np.sin(x)
	y2 = np.cos(x)

	plt.plot(x, y1)     # curve 1
	plt.plot(x, y2)     # curve 2 
	plt.plot(x, y1 + y2)       # curve 3
	plt.show()

def multiple2():
	x = np.linspace(0, 2 * np.pi , 100)
	y1 = np.sin(x)
	y2 = np.cos(x)
	plt.plot(x, y1)
	plt.plot(x, y2)
	plt.plot(x, y1 + y2)
	plt.legend(["sin(x)", "cos(x)", "sin(x) + cos(x)"], loc=2)  # legend at upper left corner
	plt.show()

def multiple3():
	plt.figure(figsize=(10, 3))
	plt.plot([1, 2, 3], [2, 4, 3], linewidth = 6)
	plt.title('very wide figure')
	#plt.savefig('output/fig1.png') # do not change, saving to output folder 
	plt.figure()  # new figure of default size
	plt.plot([1, 2, 3], [1, 3, 1], 'r')
	plt.title('second figure')
	plt.show()
	#plt.savefig('output/fig2.png')   # do not change, saving to output folder

def multiple4():
	x = np.linspace(0, 2 *np.pi , 100)
	y1 = np.sin(x)
	fig, ax = plt.subplots()
	ax.plot(x, y1)
	ax.set_xlabel('x') 
	ax.set_ylabel('y') 
	ax.set_title('y = sin(x)')
	plt.show()
#multiple1()
#multiple2()
#multiple3()
#multiple4()

#plotting multiple curves on the same plot
def curves1():
	x = np.linspace(0, 2 * np.pi , 100)
	y1 = np.sin(x)
	y2 = np.cos(x)

	plt.plot(x, y1)     # curve 1
	plt.plot(x, y2)     # curve 2 
	plt.plot(x, y1 + y2)       # curve 3
	plt.show()

def curves2():
	x = np.linspace(0, 2 * np.pi , 100)
	y1 = np.sin(x)
	y2 = np.cos(x)

	plt.plot(x, y1)
	plt.plot(x, y2)
	plt.plot(x, y1 + y2)
	plt.legend(["sin(x)", "cos(x)", "sin(x) + cos(x)"], loc=2)  # legend at upper left corner
	plt.show()

def curves3():
	plt.figure(figsize=(10, 3))
	plt.plot([1, 2, 3], [2, 4, 3], linewidth = 6)
	plt.title('very wide figure')
	plt.savefig('output/fig1.png') # do not change, saving to output folder 

	plt.figure()  # new figure of default size
	plt.plot([1, 2, 3], [1, 3, 1], 'r')
	plt.title('second figure');
	plt.savefig('output/fig2.png')   # do not change, saving to output folder
	plt.show()

def curves4():
	x = np.linspace(0, 2 *np.pi , 100)
	y1 = np.sin(x)

	fig, ax = plt.subplots()
	ax.plot(x, y1)
	ax.set_xlabel('x') 
	ax.set_ylabel('y') 
	ax.set_title('y = sin(x)')
	plt.show()

#curves1()
#curves2()
#curves3()
#curves4()

def subplots1():
	x = np.linspace(0, 2 * np.pi , 100)
	y1 = np.sin(x)
	y2 = np.cos(x)

	fig, ax = plt.subplots(2, 2, figsize=(9, 5)) # creates a 2x2 grid

	ax[0, 0].plot(x, y1) # plots on [0, 0] block on the grid
	ax[0, 0].set_title("sin(x)") 

	ax[0, 1].plot(x, y2) # plots on the [0, 1] block on the grid 
	ax[0, 1].set_title("cos(x)") 

	ax[1, 0].plot(x, y1 + y2) # plots on [1, 0] block on the grid
	ax[1, 0].set_title("sin(x) + cos(x)") 

	ax[1, 1].plot(x, y1 - y2) # plots on the [1, 1] block on the grid 
	ax[1, 1].set_title("sin(x) - cos(x)") 

	fig.tight_layout() 
	plt.show()

def subplots2():
	x = np.linspace(0, 2 * np.pi , 100)
	y1 = np.sin(x)
	y2 = np.cos(x)
	fig = plt.figure(figsize=(9, 5)) # creates a figure
	# we are using a 2x2 grid
	ax1 = fig.add_subplot(221)      # creates axis at index 1
	ax1.plot(x, y1)
	ax1.set_title("sinx(x)")

	ax2 = fig.add_subplot(222)      # creates axis at index 2
	ax2.plot(x, y2)
	ax2.set_title("cos(x)")

	ax3 = fig.add_subplot(223)      # creates axis at index 3
	ax3.plot(x, y1 + y2)
	ax3.set_title("sin(x) + cos(x)")

	ax4 = fig.add_subplot(224)       # creates axis at index 4
	ax4.plot(x, y1 - y2)
	ax4.set_title("sin(x) - cos(x)")   

	fig.tight_layout() 
	plt.show()

#subplots1()
#subplots2()

#setting up the axes
def axes1():
	x = np.linspace(-5, 5, 100)
	fig, axes = plt.subplots(3, 1, figsize=(8, 8))
	axes[0].plot(x, 2 * x + 2, x, 2 * x + 4)
	axes[0].set_title("default axes")

	axes[1].plot(x, 2 * x + 2, x, 2 * x + 4)
	axes[1].axis('tight') 
	axes[1].set_title("tight axes")

	axes[2].plot(x, 2 * x + 2, x, 2 * x + 4)
	axes[2].set_ylim([-10, 10])     # setting x
	axes[2].set_xlim([-2, 2])
	axes[2].set_title("custom axes");

	fig.tight_layout() 
	plt.show()

def logaxes():
	x = np.linspace(0, 10, 100)
	y = np.exp(2 * x)

	fig, axes = plt.subplots(1, 2, figsize=(12, 8))

	axes[0].plot(x, y)
	axes[0].set_title("Normal")

	axes[1].plot(x, y)
	axes[1].set_yscale('log') # setting yscale to log
	axes[1].set_title("Logarithmic")
	plt.show()

def grid():
	x = np.linspace(-10, 10, 100)
	y = x**2 + (2 * x) + 6

	fig, axes = plt.subplots(1, 2, figsize=(12, 8))

	axes[0].plot(x, y)
	axes[0].grid(True)
	axes[0].set_title("Deafult Grid")

	axes[1].plot(x, y)
	axes[1].grid(color='g', linewidth=1, linestyle='dashed')
	axes[1].set_title("Custom Grid")
	plt.show()

def propchange():
	x = np.linspace(-10, 10, 100)
	y = x**2 + (2 * x) + 6

	fig, axes = plt.subplots(figsize=(12, 8))
	axes.spines['top'].set_color('r')   # setting color of top spine
	axes.spines['bottom'].set_color('b')    # setting color of bottom spine
	axes.spines['bottom'].set_linewidth(2)  # setting linewidth of bottom spine
	axes.spines['left'].set_color('g')     # setting color of left spine
	axes.plot(x, y)
	plt.show()

def twinaxes():
	t = np.linspace(0, np.pi/100, 100)    # an array of time
	print(t)
	W = 2 * np.pi * 50             # angular frequency
	theta = np.pi/2    # phase difference

	I = 5 * np.sin(W * t)   # values of current
	V = 24 * np.sin(W * t + theta)   # values of voltage

	fig, axesI = plt.subplots(figsize=(12, 8))

	axesI.plot(t, I, 'r')
	axesI.set_xlabel("time(s)")
	axesI.set_ylabel("Current(A)", color='red')

	axesV = axesI.twinx()  # instantiate a second axes that shares the same x-axis

	axesV.plot(t, V, 'b')
	axesV.set_ylabel("Voltage(V)", color='blue') 
	plt.show()

def ticks():
	t = np.linspace(0, 2 * np.pi, 100)    
	I = 5 * np.sin(t)   

	fig, axes = plt.subplots(figsize=(12, 8))

	axes.plot(t, I, 'r')
	axes.set_xlabel("time(s)")
	axes.set_ylabel("Current(A)")

	axes.set_xticks(np.linspace(0, 2 * np.pi, 5)) # specifying ticks
	axes.set_xticklabels(['0', r'$0.5\pi$', r'$\pi$', r'$1.5\pi$', r'$2\pi$' ]) # custom ticks
	plt.show()

#axes1()
#logaxes()
#grid()
#propchange()
#twinaxes()
#ticks()

#Gallery of Graphs

def pie():
	genre = ['Drama', 'Comedy', 'Thriller', 'Sci-Fi', 'History']
	amount = [100, 25, 30, 70, 75]
	pieColor = ['MediumBlue', 'SpringGreen', 'BlueViolet'];

	plt.axis('equal')
	plt.pie(amount, labels=genre, autopct='%1.1f%%', colors=pieColor)
	plt.show()

def histogram():
	n = np.random.randn(100000)
	fig, axes = plt.subplots(figsize=(12, 8))
	plt.hist(n)
	axes.set_title("Histogram")
	axes.set_xlim((min(n), max(n)))
	plt.show()

def bar():
	y = np.random.randint(low=1, high=100, size=10)
	x = np.arange(10)
	fig, axes = plt.subplots(figsize=(12, 8))
	axes.bar(x, y)
	axes.set_xticks(np.arange(10))
	axes.set_title("Bar Chart")
	plt.show()

def box():
	data1 = np.random.randint(low=1, high=100, size=50)
	data2 = np.random.randint(low=1, high=100, size=50)
	data = [data1, data2]
	fig, axes = plt.subplots(figsize=(12, 8))

	axes.boxplot(data)
	axes.set_title("Box Plot")
	plt.show()

def polar():
	theta = np.linspace(0, 2 * np.pi , 100)
	r = np.sin(50 * theta) * np.cos(50 * theta) 
	fig = plt.figure()
	ax = fig.add_subplot(111, polar=True) 
	ax.plot(theta, r)
	plt.show()

def fillbet():
	x = np.linspace(0, 10, 100)
	fig, axes = plt.subplots(figsize=(12, 8))
	axes.fill_between(x, 2 * x**2, x**2)
	plt.show()

def scatter():
	x = np.linspace(0, 10, 100)
	y = np.random.randint(low=1, high=100, size=100)    # creates a random array of 100 intergers 
	                                                    # ranging from 1 - 100
	fig, axes = plt.subplots(figsize=(12, 8))
	axes.scatter(x, y, marker='.')
	plt.show()

#pie()
#histogram()
#bar()
#box()
#polar()
#fillbet()
#scatter()

#3D Plots
def spiral(a, b, t):
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    return x, y, z

def woah():
	t = np.linspace(0, 20, 100)
	x1, y1, z1 = spiral(4, 1, t)
	x2, y2, z2 = spiral(2, 2, t)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(x1, y1, z1)
	ax.plot(x2, y2, z2)
	plt.show()

def func(x, y):
  z = np.sin(np.sqrt(x ** 2 + y ** 2))
  return z 

def pretty():
	x = np.linspace(-6, 6, 30)
	y = np.linspace(-6, 6, 30)
	X, Y = np.meshgrid(x, y)
	Z = func(X, Y)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(X, Y, Z, cmap=cm.cool)
	plt.show()

def woah2():
	t = np.linspace(0, 20, 100)
	x, y, z = spiral(4, 2, t)

	fig = plt.figure()

	ax1 = fig.add_subplot(121, projection='3d')
	ax1.plot(x, y, z)
	ax1.view_init(45, 45)

	ax2 = fig.add_subplot(122, projection='3d')
	ax2.plot(x, y, z, color='r')
	ax1.view_init(30, 90)
	plt.show()
#woah()
#pretty()
#woah2()

#excercises
#ex1- plotting temps

def temps():
	land_temp = np.array([6, 7, 8, 10, 14, 16, 18, 17, 15, 12, 11, 9])
	sea_temp = np.array([4, 5, 10, 11, 12, 16, 19, 18, 14, 10, 8, 5])

	fig, ax = plt.subplots(2, 1)
	ticks = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

	x = np.linspace(0, 13, 12)
	# commands for plotting the first graph
	ax[0].plot(x, land_temp, 'r', label = 'air temp')
	ax[0].plot(x, sea_temp, 'b', label = 'sea temp')
	ax[0].set_xticks(x) 
	ax[0].set_xticklabels(ticks)
	ax[0].legend(loc = 'best')
	ax[0].set_ylabel('temp (Celsius)')
	ax[0].set_xlabel('months')

	# commands for plotting the second graph
	ax[1].plot(x, land_temp - sea_temp, 'b-o')
	ax[1].set_xticks(x) 
	ax[1].set_xticklabels(ticks)
	ax[1].set_ylabel('land - sea temp (Celsius)')
	ax[1].set_xlabel('months')

	# to prevent overlap in plots
	fig.tight_layout()
	plt.show()

temps()

#ex 2 - plotting torus


# defining function
def torus(r, R, theta, phi):
  x = (R + r * np.cos(theta)) * np.cos(phi)
  y = (R + r * np.cos(theta)) * np.sin(phi)
  z = r * np.sin(theta)
  return x, y, z

# initializing values of arrays
def torus_plot():
	angle = np.linspace(0, 2 * np.pi, 100)
	theta, phi = np.meshgrid(angle, angle)
	x, y, z = torus(1, 2, theta, phi)

	# initializing figure
	fig = plt.figure(figsize = (12, 8))

	# plotting commands for first plot
	ax1 = fig.add_subplot(1, 2, 1, projection = '3d')
	ax1.plot_surface(x, y, z, cmap = cm.cool)
	ax1.view_init(36, 26)
	ax1.set_zlim(-3, 3)

	# plotting commands for second plot
	ax2 = fig.add_subplot(1, 2, 2, projection = '3d')
	ax2.plot_surface(x, y, z, cmap = cm.rainbow)
	ax2.view_init(15, 45)
	ax2.set_zlim(-3, 3)
	plt.show()

torus_plot()

