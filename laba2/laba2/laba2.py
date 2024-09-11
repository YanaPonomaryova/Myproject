import math

# Функція для обчислення значення z
def calculate_z(m):
    if m <= 0:
        return "m must be a positive number!"
    return 1 / (math.sqrt(m) + math.sqrt(2))

# Функція для перевірки, чи є число n простимF
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    m = float(input("Enter a number m: "))
    z = calculate_z(m)
    print(f"Value of z: {z}")

    n = int(input("Enter a number n to check: "))
    if is_prime(n):
        print(f"Number {n} is prime.")
    else:
        print(f"Number {n} is not prime.")

if __name__ == "__main__":
    main()

