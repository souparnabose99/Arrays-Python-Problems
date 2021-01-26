# Check whether a string is a palindrome or not
def is_palindrome(string):
    rev = reverse(string)
    if rev == string:
        print('True')
        return True
    print('False')
    return False


def reverse(string):
    data = list(string)
    startIndex = 0
    endIndex = len(data)-1
    while startIndex < endIndex:
        data[startIndex], data[endIndex] = data[endIndex], data[startIndex]
        startIndex += 1
        endIndex -= 1
    return ''.join(data)


if __name__ == '__main__':
    s = 'Car'
    is_palindrome(s)
    s2 = 'radar'
    is_palindrome(s2)