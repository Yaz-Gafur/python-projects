# Function to find the square root of a number using the bisection method
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Check if the input is negative and raise an error if so
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers.")
    
    # Handle the special case when the input is 1
    if square_target == 1:
        root = 1  # The square root of 1 is 1
        print(f"Square root of {square_target} is 1")
    
    # Handle the special case when the input is 0
    elif square_target == 0:
        root = 0  # The square root of 0 is 0
        print(f"Square root of {square_target} is 0")
    
    # For other cases, proceed with the bisection method
    else:
        # Set the initial bounds for the bisection search
        low = 0
        high = max(1, square_target)  # Ensures that high is at least 1 for numbers between 0 and 1
        root = None  # Initialize root to None to check convergence later

        # Iterate up to the maximum number of allowed iterations
        for _ in range(max_iterations):
            # Calculate the midpoint of the current bounds
            mid = (low + high) / 2
            # Calculate the square of the midpoint
            square_mid = mid ** 2

            # Check if the difference between the square and target is within the tolerance
            if abs(square_mid - square_target) < tolerance:
                root = mid  # Set the root to the midpoint if the result is sufficiently close
                break  # Exit the loop as the solution is found
            elif square_mid < square_target:
                low = mid  # Adjust the lower bound if the midpoint square is less than the target
            else:
                high = mid  # Adjust the upper bound if the midpoint square is greater than the target
        
        # Check if the root was found after all iterations
        if root is None:
            print(f"Failed to converge within the {max_iterations} iterations.")
        else:
            # Print the result when the root is found
            print(f"Square root of {square_target} is approximately {root}")
    
    # Return the calculated square root
    return root

# Define the number for which the square root is to be found
N = 24

# Call the function to find the square root of N
square_root_bisection(N)
