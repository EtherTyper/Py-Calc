>>> from sympy import *
>>> x, y, z = symbols('x, y, z')
>>> solve(x**2+6*x+9)
[-3]
>>> roots(x**2+6*x+9)
{-3: 2}
>>> diff(x**3+6*x**2+9*x+10)
3*x**2 + 12*x + 9