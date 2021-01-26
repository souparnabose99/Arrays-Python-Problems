# Reversing an array
def reverse(arr):
    startIndex = 0
    endIndex = len(arr) - 1
    while startIndex < endIndex:
        '''temp = arr[startIndex]
        arr[startIndex] = arr[endIndex]
        arr[endIndex] = temp'''
        arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]
        startIndex += 1
        endIndex -= 1
    return arr


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    print(array)
    rev = reverse(array)
    print(rev)
    array2 = [-1, -2, -3, -4]
    print(array2)
    rev2 = reverse(array2)
    print(rev2)

