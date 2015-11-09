>>> from sympy import *
>>> x, y, z = symbols('x, y, z')
>>> solve(x**2 - 6*x**2 + 9*x, x)
[0, 9/5]
>>> roots(x**2 - 6*x**2 + 9*x, x)
{0: 1, 9/5: 1}
>>> solve(x**3 - 6*x**2 + 9*x, x)
[0, 3]
>>> roots(x**3 - 6*x**2 + 9*x, x)
{0: 1, 3: 2}