# Reversing an integer
def int_reversal(n):
    remainder = 0
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = n // 10
    return reverse


if __name__ == '__main__':
    num = 123456789123456789123456789
    print(num)
    num = int_reversal(num)
    print(num)


