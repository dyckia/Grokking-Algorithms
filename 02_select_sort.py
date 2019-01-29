def findSmallest(l):
    smallest_ind = 0
    smallest = l[smallest_ind]
    for i in range(1, len(l)):
        if l[i] < smallest:
            smallest_ind = i
            smallest = l[smallest_ind]
    return smallest_ind


def select_sort(l):
    sorted_l = []
    for i in range(len(l)):
        smallest_ind = findSmallest(l)
        sorted_l.append(l.pop(smallest_ind))
    return(sorted_l)


if __name__ == '__main__':
    l = [54, 23, 56, 78, 78, 21]
    sorted_l = select_sort(l)
    print(sorted_l)
