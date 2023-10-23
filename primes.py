"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer")
    
    primes_list = []
    num = 2  # start with the first prime number
    
    while len(primes_list) < number_of_primes:
        # Assume num is prime until shown it is not. 
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # check all divisors up to the square root of num
            if num % i == 0:
                is_prime = False  # num is divisible by some number, so it's not prime
                break

        if is_prime:
            primes_list.append(num)  # num is prime, so add it to the list

        num += 1  # move to the next number

    return primes_list

# Example usage:
try:
    print(primes(10))  # Should print: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
except ValueError as e:
    print(e)
