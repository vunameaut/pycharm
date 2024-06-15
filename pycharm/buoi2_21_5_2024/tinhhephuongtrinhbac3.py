from sympy import symbols, Eq, solve



x, y, z = symbols('x y z')

eq1 = Eq(x + y + z, 20)
eq2 = Eq(2 * x + y - z, 10)
eq3 = Eq(x - y + 2 * z, 1)

solution = solve((eq1, eq2, eq3), (x, y, z))
print(solution)

 
    