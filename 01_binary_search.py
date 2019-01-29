def binary_search(list, num):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if num == list[mid]:
            return(print('Found value {} at index {}'.format(num, mid + 1)))
        elif num > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return(print('Couldn\'t find value {} in list {}'.format(num, list)))


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    num = 5
    binary_search(list, num)
