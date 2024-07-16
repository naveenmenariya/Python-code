import sympy as sp

def secant_method(func, x0, x1, tol=1e-8, max_iter=100):
    x = [x0, x1]
    f = sp.lambdify('x', func)  # Convert sympy expression to a function
    
    for i in range(max_iter):
        x_new = x[-1] - f(x[-1]) * (x[-1] - x[-2]) / (f(x[-1]) - f(x[-2]))
        x.append(x_new)
        
        if abs(x[-1] - x[-2]) < tol:
            return x[-1]
    
    return x[-1]

# Example usage:
if __name__ == "__main__":
    x = sp.symbols('x')
    user_func = input("Enter your function in terms of 'x': ")
    try:
        expr = sp.sympify(user_func)
        minimizer = secant_method(expr, 0, 1)  # Initial guesses x0=0, x1=1
        print(f"The minimizer is approximately: {minimizer}")
    except sp.SympifyError:
        print("Invalid input. Please enter a valid function.")
