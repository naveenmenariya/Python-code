import sympy as sp

def newton_minimizer():
    # Get the function from the user
    function_input = input("Enter a function in terms of 'x': ")
    x = sp.symbols('x')
    try:
        # Parse the user-input function
        user_function = sp.sympify(function_input)
        
        # Find the derivative of the function
        derivative = sp.diff(user_function, x)
        
        # Convert the function and derivative to lambdified functions for numerical evaluation
        f = sp.lambdify(x, user_function)
        f_prime = sp.lambdify(x, derivative)
        
        # Initial guess for the minimizer
        guess = float(input("Enter an initial guess for the minimizer: "))
        
        # Newton's method iterations
        max_iterations = 100
        tolerance = 1e-8
        iteration = 0
        while abs(f(guess)) > tolerance and iteration < max_iterations:
            guess = guess - f(guess) / f_prime(guess)
            iteration += 1
        
        if iteration == max_iterations:
            print("Maximum iterations reached. No solution found.")
        else:
            print(f"The minimizer is approximately at x = {guess} with function value {f(guess)}.")
    
    except (sp.SympifyError, ValueError) as e:
        print("Invalid input. Please enter a valid function and initial guess.")

# Run the function
newton_minimizer()
