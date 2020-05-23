array = [14, 44, 7, 13, 87, 18, 33, 6, 58, 10]


def shell_sort(arr):

    sublistcount = len(arr) // 2

    while sublistcount > 0:
        for start in range(sublistcount):

            gap_insertion_sort(arr, start, sublistcount)

        sublistcount = sublistcount // 2

    print(arr)


def gap_insertion_sort(arr, start, sublistcount):

    for i in range(start + sublistcount, len(arr), sublistcount):

        current_value = arr[i]
        position = i

        while position >= sublistcount and arr[position - sublistcount] > current_value:

            arr[position] = arr[position - sublistcount]
            position = position - sublistcount

        arr[position] = current_value


shell_sort(array)


