
def is_prime(n: int) -> bool:
    factors = get_factors(n)
    if len(factors) <= 1: return False
    return all(factor == 1 or factor == n for factor in factors)

def get_factors(n: int) -> list[int]:
    factors = []
    if(n == 0): 
        factors.append(0)
        return factors
    i = 1
    while i <= n:
        if n % i == 0: factors.append(i)
        i = i + 1
    return factors

def main():
    n = int(input("Enter an integer here to get its prime factors: "))
    factors = get_factors(n)
    prime_factors = []
    for num in factors:
        if is_prime(num): prime_factors.append(num)
    print(f"The prime factors of {n} are: ", end = "")
    for num in prime_factors:
        print(f"{num}, ", end = "")
    print("")

if __name__ == "__main__":
    main()