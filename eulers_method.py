# Computes approximate solutions to differential equations of the form dy/dx = f(y) using Euler's method
# (also known as autonomous or time-invariant systems)

import matplotlib.pyplot as plt
import numpy as np

def calculate_next_point(last_point, delta, derivative_function):
    '''Calculates the next point given the last point, a delta and the derivative function'''
    return [last_point[0] + delta, last_point[1] + derivative_function(last_point[1]) * delta]

def compute_approximate_solution(initial_point, delta, derivative_function, end_x):
    '''Computes an approximate solution to the given differential equation'''
    solution = [initial_point]

    while solution[-1][0] < end_x:
        solution.append(calculate_next_point(solution[-1], delta, derivative_function))
    
    return solution

# User input ------------------------------------------------------------

# The f(y) in our equation (the function that gives the derivative)
user_function_string = input('Enter an expression for f(y) in the equation dy/dx = f(y): ')
user_function = compile('x = ' + user_function_string, 'user', 'single')
def f(i):
    ns = {'y': i}
    exec(user_function, ns)
    print(ns['x'])
    return ns['x']

# The initial value of the function
initial_point = input('Initial point of the form <x,y> for the approximation [enter for <0,3>]').split(',')
if initial_point == ['']:
    initial_point = [0, 3]
else:
    initial_point = [float(x) for x in initial_point]

# The various 'delta x's to use in Euler's method
deltas = input('List of deltas of the form <x,y,z> [press enter for <2,1,0.1>]: ').split(',')
if deltas == ['']:
    deltas = [2, 1, 0.1]
else:
    deltas = sorted([float(x) for x in deltas], reverse=True)

# The last x value we want to compute (the length of the approximation)
end_x = float(input('Greatest x value for the approximation: '))

# Compute the approximations with different deltas
solutions = [compute_approximate_solution(initial_point, d, f, end_x) for d in deltas]

# Isolate x and y
xs = [[n[0] for n in s] for s in solutions]
ys = [[n[1] for n in s] for s in solutions]

# Plot result ------------------------------------------------------------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Helvetica Neue'
plt.rcParams['font.size'] = 10
plt.style.use('fivethirtyeight')

for i in range(len(solutions)):
    plt.plot(xs[i], ys[i], label='delta = ' + str(deltas[i]))

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Approximations to y(x)')
plt.legend()
plt.show()