from sympy import symbols, parse_expr, Derivative
import pandas as pd

x = symbols('x')

expression = input("Expression: ")

eq = parse_expr(expression)
print(eq)

deq = Derivative(eq, x).doit()
print(deq)

a = float(input("Enter the first limit: "))
b = float(input("Enter the second limit: "))
acc = int(input("Enter the number of digits of accuracy: "))
oa = a
ob = b
up = []
low = []
clist = []
f_min = float('inf')  # Initializing f_min with infinity

while True:

    c = round((((deq.subs(x, b)) * a) - ((deq.subs(x, a)) * b)) / ((deq.subs(x, b) - (deq.subs(x, a)))), acc)

    low.append(a)
    up.append(b)
    clist.append(c)

    a = round(b, acc)
    b = round(c, acc)
    
    # Evaluate the function at the current point 'c'
    f_c = eq.subs(x, c)
    
    # Check if the function value at 'c' is less than the current minimum
    if f_c < f_min:
        f_min = f_c
        min_point = c

    if round(a, acc) == round(b, acc):
        res = round(min_point, acc)
        break

data = {'Lower Limit': low,
        'Upper Limit': up,
        'Next Value': clist}
df = pd.DataFrame(data)

print(df)
print()
print(f"Minimum value of the function {expression} in the interval [{oa},{ob}] is {f_min} at x = {res}")
