import math
from datetime import datetime

def main():
    RANGE = 10**8
    NUMBERS = [True] * (RANGE - 1)
    PRIMES = []
    
    n = 2
    limit = math.sqrt(RANGE)
    while n <= limit:
        if NUMBERS[n - 2]:
            PRIMES.append(n)
            for j in range(n * n, RANGE, n):
                NUMBERS[j - 2] = False
        n += 1
    
    # Collect remaining prime numbers
    for i in range(n, RANGE):
        if NUMBERS[i - 2]:
            PRIMES.append(i)
    
    print("--Sieve Of Eratosthenes--")
    print("Number of primes:", len(PRIMES))

if __name__ == "__main__":
    start = datetime.now()
    main()
    print(datetime.now() - start)
