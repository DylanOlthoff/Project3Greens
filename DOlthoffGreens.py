# Dylan Olthoff
# CST-305
# Dr.Ricardo Citro
# Topic 3 Project 3: Green's Function and ODE with IVP
# Part 2: solving the homogeneous from part 1 and plot
# Implementation:
# made functions using scipy and green's function
# graphed functions

#imported packages
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ODE
def d1dx(U, x):
    return [U[1], -2 * U[1] + 2 * x - 2]    # returns y' and -2y' + 2x -2

def d2dx(U, x):
    return [U[1], 4 - U[0]]     # returns y' and 4 - y

# Green's
def greens1(x):
    return (0.5 * pow(x, 2)) - (1.5 * x) - (np.exp(-2 * x)) + 1 # returns y(x) = 1/2(x^2) - 1.5x - e^(-2x) + 1

def greens2(x):
    return 4 - (4 * np.cos(x)) # returns y(x) = 4 - (4 * np.cos(x))

# time analysis
timeStart1 = 0
timeEnd1 = 0
t0 = 0
timeStart2 = 0
timeEnd2 = 0
t1 = 0
timeStart3 = 0
timeEnd3 = 0
t2 = 0
timeStart4 = 0
timeEnd4 = 0
t3 = 0

# ODEint answers
timeStart1 = time.time()

U0 = [0, 0]   # vector to hold y and y' values
xs0 = np.linspace(0, 50, 1000)  # x space
ys0 = odeint(d1dx, U0, xs0)   # y space with odeint
ys0 = ys0[:,0]

timeEnd1 = time.time()               # time to complete
t0 = timeEnd1 - timeStart1

timeStart2 = time.time()

U1 = [0, 0]   # vector to hold y and y' values
xs1 = np.linspace(0, 50, 1000)  # x space
ys1 = odeint(d2dx, U1, xs1)   # y space with odeint
ys1 = ys1[:,0]

timeEnd2 = time.time()   # time to complete
t1 = timeEnd2 - timeStart2

# Green's solutions
n = 2000 # initial values
h = 0.025

x0 = 0 # variables for x spaces
x1 = 0
y0 = 0 # variables for y spaces
y1 = 0

xs2 = [] # variables for x spaces
xs3 = []
ys2 = [] # variables for y spaces
ys3 = []

timeStart3 = time.time()

for i in range(n):  # loops greens function
    xs2.append(x0)   # add x value to x space
    ys2.append(y0)  # add y value to y space
    y0 = greens1(x0)  # change the y value with greens
    x0 += h          # change x value moving a step forward

timeEnd3 = time.time()   # time to complete
t2 = timeEnd3 - timeStart3

timeStart4 = time.time()

for i in range(n):    # loops greens function
    xs3.append(x1)   # add x value to x space
    ys3.append(y1)  # add y value to y space
    y1 = greens2(x1)  # change the y value with greens
    x1 += h          # change x value moving a step forward

timeEnd4 = time.time()               # time to complete
t3 = timeEnd4 - timeStart4

# print time analysis

print("odeint 1 time: " + str(t0))
print("odeint 2 time: " + str(t1))

print("greens 1 time: " + str(t2))
print("greens 2 time: " + str(t3))

# graphs

plt.title("1. ODE and Green's Functions Analysis")     # title of graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs0, ys0, 'r-', label = "ODEint 1", linewidth = 2) # set the ODE line to be red and label it
plt.plot(xs2, ys2, 'b-', label = "Green's Function 1")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # show graph

plt.title("1. ODE Function Analysis")                  # title of graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs0, ys0, 'r-', label = "ODEint 1", linewidth = 2) # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # show graph

plt.title("1. Green's Functions Analysis")             # title of graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs2, ys2, 'b-', label = "Green's Function 1")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # show graph

plt.title("2. ODE and Green's Functions Analysis")     # title of graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs1, ys1, 'r-', label = "ODEint 2", linewidth = 2) # set the ODE line to be red and label it
plt.plot(xs3, ys3, 'b-', label = "Green's Function 2")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # show graph

plt.title("2. ODE Function Analysis")                  # title of graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs1, ys1, 'r-', label = "ODEint 2", linewidth = 2) # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # show graph

plt.title("2. Green's Functions Analysis")             # title of graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs3, ys3, 'b-', label = "Green's Function 1")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # show graph