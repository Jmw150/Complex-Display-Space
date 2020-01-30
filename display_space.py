#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from cmath import * # complex number arithmetic
import random
import argparse # Useful for command line 

def color ():
    string = '#'
    for i in range(0,6):
        string += str(random.randint(0,9))
    return string


def line (x_start,y_start,x_end,y_end) :
    # define iterations
    dt = .01 # timestep
    x, y = [] , []
    if x_end == x_start :
        t = np.arange(y_start, y_end, dt)
        for i in t:
            x.append(x_start)
            y.append(i)
    elif x_end > x_start :
        m = (y_end - y_start)/(x_end - x_start)
        t = np.arange(x_start, x_end, dt)
        for i in t:
            x.append(i)
            y.append(m*(i-x_start)+y_start)
    elif x_end < x_start :
        # swap the values
        temp = x_end
        x_end = x_start
        x_start = temp
        temp = y_end
        y_end = y_start
        y_start = temp

        m = (y_end - y_start)/(x_end - x_start)
        t = np.arange(x_start, x_end, dt)
        for i in t:
            x.append(i)
            y.append(m*(i-x_start)+y_start)
        
    return x,y


def grid(bottom_l_x,bottom_l_y,top_r_x,top_r_y,res) :
    total = []
    dt = abs(top_r_x - bottom_l_x)/res
    # vertical lines first
    t = np.arange(bottom_l_x, top_r_x+dt, dt) # has one extra line to make it a box
    #print(t)
    for i in t :
        total.append(line(i,bottom_l_y,i,top_r_y))

    # horizontal
    t = np.arange(bottom_l_y, top_r_y+dt, dt) # has one extra line to make it a box
    #print(t)
    for i in t :
        total.append(line(bottom_l_y,i,top_r_y,i))

    return total


def cmap(w,d) :
    # w = complex function
    # d = domain
    x, y = [],[]
    # move [x vector, y vector] -> [(x_i,y_i),...]
    tup = []
    for i in range(len(d[0])) :
        tup.append([d[0][i],d[1][i]])
    for i,j in tup:
        x.append(w(i,j).real)
        y.append(w(i,j).imag)

    return x,y

def cmap_m(w,D) :
    " assume this is a set of plots, instead of a single plot"
    total = []
    for d in D :
        total.append(cmap(w,d))
    
    return total

def Plot(f) :
    plt.plot(f[0],f[1],color()) # may colide but unlikely

def Plot_multiple(f) :
    for i in f:
        plt.plot(i[0],i[1],color()) # may colide but unlikely


if __name__ == '__main__':

    # make sense of user input from a terminal
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', type=str,
        help='Enter complex number function',
        default="(x+1j*y)" )

    arg = parser.parse_args()


    header = str(arg.function)#"exp(x+1j*y)"
    w = lambda x,y : eval(header) 

    Plot_multiple(cmap_m(w,grid(-pi,-pi,pi,pi,20)))

    plt.title(header)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.grid()
    plt.show()


#Plot(line(-1,-1,1,-1))
#Plot(line(-1,1,1,1))
#Plot(line(-1,-1,-1,1))
#Plot(line(1,-1,1,1))

#Plot(cmap(w,line(-5,e,5,e)))
#Plot(cmap(w,line(-1,1,1,1)))
#Plot(cmap(w,line(-1,-1,-1,1)))
#Plot(cmap(w,line(1,-1,1,1)))

#Plot_multiple(grid(-1,-1,1,1,3))
