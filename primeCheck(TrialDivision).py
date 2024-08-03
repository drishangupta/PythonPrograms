import math
from datetime import datetime
PRIME = []
def is_prime(n):
    limit = math.sqrt(n)
    for i in PRIME:
        if i>limit:
            return True
        if n % i==0:
            return False
    return True
def main():
    RANGE = 10**8
    n = 0
    t=datetime.now()
    for i in range(2,RANGE):
        if is_prime(i):
            PRIME.append(i)
            
            n+=1
    t2=datetime.now()-t
    print("Trial Division")
    print(f"Found {n} primes up to {RANGE}")
    print(f"{t2} is the time taken")
if __name__ == "__main__":
    main()