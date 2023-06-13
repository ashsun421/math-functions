def exponentiate(a, b):
    num = a
    for i in range (b-1):
         a *= num
    return a
print(exponentiate(2,4))

def factorial(n):
    ans = 1
    for i in range(n):
        ans = ans * (i+1)
    return ans
print(factorial(4))

def permutation(n, r):
    return factorial(n) / factorial(n - r)

print(permutation(6, 4))

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))
print(combination(6, 4))

def is_it_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_it_prime(12))

def prime_factors(n):
    prime = []
    for i in range(n):
        if n % (i+1) == 0:
            if is_it_prime(i+1) == True:
                prime.append(i+1)
    return prime
        
print(prime_factors(63))
