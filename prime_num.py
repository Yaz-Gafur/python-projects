def is_prime(n):
    # Check if the number is less than 2 (as prime numbers start from 2)
    if n < 2:
        return False

    # Check divisibility from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If divisible, it's not a prime
            return False

    return True  # If no divisors found, it is a prime number


#1 __Edge Case (n < 2): Any number less than 2 is not a prime.
#2 __Check for Divisibility: The function loops through numbers from 2 to the square root of n to check if n is divisible by any of them. If n is divisible by any number, it is not prime.
#3 __Efficiency: Checking divisibility only up to the square root of n makes the function more efficient because if a number has divisors, at least one of them will be smaller than or equal to the square root.
