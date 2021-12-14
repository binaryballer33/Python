def majority_element(nums):

    size_of_array_divided_by_two = len(nums) / 2

    number_dictionary = {}

    for number in nums:
        if number not in number_dictionary:
            number_dictionary[number] = 1
        else:
            number_dictionary[number] += 1

        if number_dictionary[number] > size_of_array_divided_by_two:
            majority_element_key = number

    return majority_element_key


majority_element_key = majority_element([1, 1, 2, 2, 1, 2, 2, 2])
print(majority_element_key)
