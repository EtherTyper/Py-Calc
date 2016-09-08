from sympy import *

x, y, z = symbols('x, y, z')
solve(x ** 2 - 6 * x ** 2 + 9 * x, x)
roots(x ** 2 - 6 * x ** 2 + 9 * x, x)
solve(x ** 3 - 6 * x ** 2 + 9 * x, x)
roots(x ** 3 - 6 * x ** 2 + 9 * x, x)
