#Write a function that takes in a number as input, and returns all of that number's prime factors as a list.
#Ex - num = 630 prime_factors = [2, 3, 3, 5, 7]

def get_prime_factors(num):
    divisor = 2
    prime_factors = []

    while num >= divisor:
        if num % divisor == 0:
            prime_factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1

    return prime_factors


print(get_prime_factors(13))