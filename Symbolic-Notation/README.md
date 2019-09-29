#

Python can also allow for symbolic representation of functions like polynomials and other such math related notation. I've just found out about it so I'd like to mess around a bit with it!


~~~Python

from sympy import *
x, y, z = symbols('x,y,z')
init_printing(use_unicode=False, wrap_line=False)

e = (x + y)*(y - 2*z)
e.as_poly()

>>> Poly(𝑥𝑦−2𝑥𝑧+𝑦2−2𝑦𝑧,𝑥,𝑦,𝑧,𝑑𝑜𝑚𝑎𝑖𝑛=ℤ)
~~~
