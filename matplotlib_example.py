# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
#                   Anderson Loan
#                   Andrew Spears
#                   Spencer Jones
# Section:         574
# Assignment:   Lab 
# Date:         15 11 2022
#
#
#improts cool stuff
# As a team, we have gone through all required sections of the # tutorial, and each team member understands the material

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from math import *
#for the first graph
x = np.arange(-2.,2.,.1)

f = [2,6]

for i in f:
    g = (1/(4*i)) * x**2
    if i == 2:
        a, = plt.plot(x,g, linewidth = i,label = "f=2",color = 'r')#plots the two parabolas with a differnt line width
    if i == 6:
        b, = plt.plot(x,g, linewidth = i,label = "f=6", color = 'b')
plt.legend(handles = [a,b], loc = "upper left")
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Parabola plots with varying focal length")

plt.show()

#for the second graph
x = np.arange(-4.,4.,.25)#creates our domain from -4 - 4 and we're using every .25 x values
y = 2*x**3 + 3*x**2-11*x - 6#sets up our y value 2 the cubic functio
plt.plot(x,y,'y*')#plots function with yellow stars
plt.title("Plot cubic polynomial")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
    
#for the third graph
plt.figure()#sets up graph so we can do sub plots
x = np.arange(-2*pi, 2*pi, 0.1)#sets up our domain to be from -2pi - 2pi and we go for ever .1 x
y = np.cos(x)#sets our y values to the function of cos(x)
plt.subplot(211)#creates our first sub plot
a, = plt.plot(x,y,'r-',label = "cos(x)")#plots grph
plt.legend(handles = [a], loc = "lower right")
y=np.sin(x)#sets up our y value to equal the function of sin(x)
plt.subplot(212)#creates 2nd sub plot
b, = plt.plot(x,y,'b-',label = "sin(x)")#plots the function
plt.legend(handles = [b], loc = "lower right")
plt.show()#shows graph






