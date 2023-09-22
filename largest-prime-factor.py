import sys

def largest_prime_factor(num, factor):
    if num / factor == 1:
        print("final factor: ", factor)
        return factor

    if factor > 1 and num % factor == 0:
        print("factor found: ", factor)
        return largest_prime_factor(num/factor, factor)

    return largest_prime_factor(num, factor+1)

sys.setrecursionlimit(100000000)
r = largest_prime_factor(600851475143, 1)

print("result: ", r)

