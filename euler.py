#Euler's method to solve initial value problems
#import Tkinter for graphics
from Tkinter import *
from math import *
from array import *

#define the step size, smaller=more accurate (float)
step_size = 0.01
#define the maximum x value 
x_max = 8.0
#define y(0)
y0 = 1
#define the y derivative
def y_prime(x,y):
    return 0.6*sin(x)
    

#calculate where the last increment is based on the specified domain
max_increments = int(x_max/step_size)
#Arrays to store calculated x and y coordinates
xArray=array('d',range(0,max_increments))
yArray=array('d',range(0,max_increments))

#Graphics stuff:
#create root and canvas
root = Tk()
width = 600
height = 600
canvas = Canvas(root,width=600,height=600)
canvas.pack()
root.canvas = canvas.canvas = canvas # Store canvas in root and in canvas itself for callbacks
#converts a cartesian coordinate to on screen coordinate for drawing (x)
def get_x_coord(x):
	center = width/2
	return x+center
#converts a cartesian coordinate to on screen coordinate for drawing (y)
def get_y_coord(y):
	center = height/2
	return center-y

#performs all of the scaling and drawing of points from xArray,yArray
# r is the radius of the dots for plotting
def draw(r):
	xMax = -float("inf")
	yMax = -float("inf")
	#find maximum value for plot scaling
	for j in range(0,max_increments):
		if(xArray[j]>xMax):
			xMax = xArray[j]
		if(yArray[j]>yMax):
			yMax = yArray[j]
	#draw axis
	canvas.create_line(0,height/2,width,height/2,dash=(3,2),fill="#a3a3a3")
	canvas.create_line(width/2,0,width/2,height,dash=(3,2),fill="#a3a3a3")
	canvas.create_text(width/2, 12, anchor=W, font="Times",text=int(round(yMax)))
	canvas.create_text(width-30, height/2+12, anchor=W, font="Times",text=int(round(xMax)))
	#print xMax
	#draw points
	for k in range(0,max_increments):
		u = get_x_coord(xArray[k]*(width/2)/xMax)
		v= get_y_coord(yArray[k]*(height/2)/yMax)
		canvas.create_oval(u-r,v-r, u+r,v+r)
	canvas.pack(fill=BOTH,expand=1)
	
	
def main():
    #start at y0
    yi = y0
    for i in range(0,max_increments):
    	yArray[i]=(yi)
    	yi = yi+step_size*y_prime(i*step_size,yi)
    	xArray[i] = (i*step_size)
    draw(0.5)
    root.mainloop()  # wait until window gets closed so graphics are displayed
        
main()