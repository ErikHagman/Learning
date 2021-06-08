import numpy
import matplotlib.pyplot as plt
import pylab
import math
from sympy import Symbol


class Fractal2D:
    
    zeroes = []

    def __init__ (self, function):
        self.f = function
        self.d = self.f.diff(x)

    def newtons_method (self, initial_guess):
    
        xn = initial_guess - (self.f/self.d)
        xn = xn.subs(x, initial_guess)
        
        A = [10, 8]
    
        for i in range (100):
            if i == 99:
                print( "This function doesnt converge with this initial guess" )
                return None
            
            elif abs(A[-1] - A[-2]) >= 0.00001:
                xn1 = xn - (self.f/self.d)
                xn1 = xn1.subs(x, xn)
                xn = xn1 
                A.append(xn1)
            
            else:
                return float(xn1)

    def task_3 (self, initial_guess):
        H = self.newtons_method(initial_guess)
        duplicate = 0
        
        if H == None:
            return

        for i in self.zeroes:
            if abs(H-i) <= 0.1:
                duplicate = True
        
        if duplicate == True:
            return
        else:
            self.zeroes.append (H)
        
       
    def plot (self):
        list_of_x0 = numpy.linspace(-20, 20, 40)
        
        for i in list_of_x0:
            self.task_3 (i)
        
        print (numpy.meshgrid(self.zeroes))
              


x = Symbol('x')

F = Fractal2D(x**2 -2)

F.plot()
