from prime_factors import is_prime

def get_primes(n: int) -> list[int]:
    i = 1
    primes = []
    while i <= n:
        if is_prime(i): primes.append(i)
        i+=1
    return primes

def main():
    primes = get_primes(1000)
    i = 0
    x = ''
    print("This program finds prime numbers. Enter quit to exit.")
    while x != 'quit': 
        if i == len(primes): return
        print(primes[i])
        i+= 1
        x = input()

if __name__ == "__main__":
    main()