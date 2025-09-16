def myPow(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        x = 1/x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x 
        n //= 2

    return result
    
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100