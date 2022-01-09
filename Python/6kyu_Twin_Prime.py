"""
A twin prime is a prime number that differs from another prime number by 2. Write a function named is_twin_prime which takes an int parameter and returns true if it is a twin prime, else false.

example:

given 5, which is prime
5+2=7 which is prime 
5-2=3 which is prime
Hence , 5 has two prime twins and its a Twin Prime.
---------------------------------------------------
given 7, which is prime
7-2=5 which is prime
7+2=9 which is not prime
Hence, 7 has one prime twin, and its a Twin Prime.
----------------------------------------------------
given 9, which is not prime 
Hence, 9 is not a Twin Prime
----------------------------------------------------
given 953 , which is prime
953-2=951 , which is not prime
953+2=955 , which is not prime 
Hence, 953 is not a Twin Prime.
"""

def is_twinprime(n):
    n_plus = int(n+2)
    n_minus = int(n-2)
    original = 0
    one = 0
    two = 0
    
    if n <= 1:
        return False
    
    for i in range(2, int(n**.5)+1):
        if (n % i == 0):
            return False
            
    for i in range(2, int(n_minus**.5)+1):
        if (n_minus % i == 0):
            one = 1
            
    for i in range(2, int(n_plus**.5)+1):
        if (n_plus % i == 0):
            two = 1
            
    if (one + two) <= 1:
        return True
    else:
        return False
    
        
