def is_prime(number):
    return False if len([i for i in range(2,int(number**0.5)+1) if number % i==0]) > 0 else True


def lower_primes(number):
    return len([i for i in range(2,number) if is_prime(i)])

def divisors(number):
    return [i for i in range(2,number) if number % i ==0]

def primal_divisors(number):
    return len([i for i in divisors(number) if is_prime(i)])

def calculate():
    number=int(input())
    weights = []
    sum_price = 0
    for i in range(number):
        weights.append(int(input()))
    for j in weights:
        if is_prime(j):
            sum_price += lower_primes(j)
        else:
            sum_price += primal_divisors(j)
    if is_prime(sum_price):
        sum_price -= lower_primes(sum_price)
    else:
        sum_price -= primal_divisors(sum_price)

    return sum_price

print(calculate())




