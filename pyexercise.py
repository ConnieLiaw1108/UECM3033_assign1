import sympy as sy
import numpy as np

def fun_1(your_id):
    ans = hex(your_id)
    return ans
    
def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate((sy.exp(x) + 2*sy.cos(sy.pi*x)), (x, 0, 1/2))
    return ans

def my_solution():
    A = np.array([[1,0,1,0,0,0,0,0,0,0], [2,0,0,0,3,0,0,0,0,0], [0,4,0,0,0,0,6,0,0,0], [0,1,0,0,0,0,0,0,0,2], [0,0,8,0,1,0,0,0,0,0], [0,0,0,0,10,0,0,0,1,0], [0,0,0,1,0,0,1,0,0,0], [0,0,0,0,0,5,0,0,0,3], [0,0,0,0,0,0,0,1,4,0], [0,0,0,0,0,2,0,9,0,0]])
    b = np.array([6,34,110,29,42,120,21,76,83,43])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x

if __name__ == '__main__':
    your_id = 1307632
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1(your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
