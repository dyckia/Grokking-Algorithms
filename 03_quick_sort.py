def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        for item in array[1:]:
            if item <= pivot:
                less.append(item)
            else:
                greater.append(item)
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    array = [32, 74, 28, 91, 21]
    s_array = quick_sort(array)
    print(s_array)
