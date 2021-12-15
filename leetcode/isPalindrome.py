class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_number = str(x)
        number_reversed = ''
        last_index = len(string_number) - 1

        for each_number in string_number:
            number_reversed += string_number[last_index]
            last_index -= 1

        if string_number == number_reversed:
            return True
        else:
            return False
