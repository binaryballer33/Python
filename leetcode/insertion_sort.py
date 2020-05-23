# array = [4, 1, 6, 3, 2]
array = [14, 44, 7, 13, 87, 18, 33, 6, 58, 10]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        # starts shifting everything over
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1

        # once everything is shifted over it will put the number in its correct spot.
        arr[position] = current_value
    print(arr)


insertion_sort(array)


