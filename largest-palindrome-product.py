def largest_palindrome_product(digits):
    if digits <= 1:
        return -1

    max = (10**digits)-1
    min = 10**(digits-1)

    largest_palindrome = 0
    for i in reversed(range(min, max+1)):
        for k in reversed(range(min, max+1)):
            p = i*k
            is_palindrome = str(p) == ''.join(reversed(str(p)))

            if p > largest_palindrome and is_palindrome:
                largest_palindrome = p

    return largest_palindrome

r = largest_palindrome_product(3)
print("result: ", r)

