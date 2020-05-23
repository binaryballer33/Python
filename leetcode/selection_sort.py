array = [14, 44, 7, 13, 87, 18, 33, 6, 58, 10]
# array = [4, 1, 6, 3, 2]

def selection_sort(arr):

    for fill_slot in range(len(arr) - 1, 0, -1):

        position_of_max = 0

        for element in range(1, fill_slot + 1):

            # is the current element the greatest element
            print(f'Is {arr[element]} > {arr[position_of_max]}?')
            if arr[element] > arr[position_of_max]:
                position_of_max = element

        # only doing the exchange once per outer loop instead of every time in the inner loop like bubble sort
        # captures the last element in the outer_loop
        temp = arr[fill_slot]
        # turns the element in the outer loop into the element at the position of max
        arr[fill_slot] = arr[position_of_max]
        # turns the element at the position of max into the element that was at the outer loop
        arr[position_of_max] = temp
        # print new array
        print(arr)


selection_sort(array)
