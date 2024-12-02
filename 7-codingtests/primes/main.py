def count_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
  
    count = 0
    for p in range(2, n+1):
        if prime[p]:
            count += 1
  
    return count

# Example usage:
n = 1000
print(count_primes(n))