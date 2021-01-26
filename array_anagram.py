# Anagram check: O(NLogN)
def is_anagram(str1, str2):
    print(str1)
    print(str2)
    if len(str1) != len(str2):
        print('False')
        return False
    str1 = sorted(str1)
    print(str1)
    str2 = sorted(str2)
    print(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print('False')
            return False
    print('String is Anagram')
    return True


if __name__ == '__main__':
    str1 = 'rowda'
    str2 = 'dowry'
    is_anagram(str1, str2)
