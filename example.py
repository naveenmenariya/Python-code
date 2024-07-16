from sympy import symbols, parse_expr, Derivative
import pandas as pd
from tabulate import tabulate

x = symbols('x')

expression = input("Expression: ")

eq = parse_expr(expression)
print(eq)

deq = Derivative(eq, x).doit()
print(deq)

d2eq = Derivative(deq, x).doit()  # Second derivative

x_val = float(input("Initial guess: "))
acc = int(input("Enter the number of digits of accuracy: "))
x_list = []

while True:
    f_val = eq.subs(x, x_val)
    f_der_val = deq.subs(x, x_val)
    
    x_list.append(x_val)
    
    x_val = round(x_val - f_der_val / d2eq.subs(x, x_val), acc)  # Newton's method for extrema
    
    if abs(f_der_val) < 10 ** -acc:  # Check for a small derivative to find a critical point
        res = round(eq.subs(x, x_val), acc)
        break

data = {'X Values': x_list}
df = pd.DataFrame(data)

print(tabulate(df, headers='keys', tablefmt='psql'))
print()
print(f"Minimum value of the function {expression} is {res} at x = {x_val}")
