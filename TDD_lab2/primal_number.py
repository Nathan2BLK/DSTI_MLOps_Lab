import math

def is_prime(num):
    # Prime numbers must be greater than 1
    if num < 2:
        return False
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True

def test_prime_composite_number():
    assert is_prime(4) == False