array = [14, 44, 7, 13, 87, 18, 33, 6, 58, 10


def bubble_sort(arr):

    print("unsorted list: ", array)

    for n in range(len(arr)-1, 0, -1):
        for o in range(n):
            # print(f'arr[o] = {arr[0]}')
            # print(f'arr[o + 1] = {arr[o + 1]}')
            print(f'is {arr[o]} > {arr[o + 1]}?)')
            if arr[o] > arr[o + 1]:
                temp = arr[o]
                print(f'Temp is arr[0]: {temp}')
                arr[o] = arr[o + 1]
                print(f'Reassigning arr[0] = {arr[o + 1]}')
                arr[o + 1] = temp
                print(f'Reassigning arr[o + 1] = {temp}')
            else:
                print("No it's not greater")

    print("sorted list:   ", array)


bubble_sort(array)
