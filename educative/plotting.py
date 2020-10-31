import numpy as np
import matplotlib.pyplot as plt


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
# curves1()