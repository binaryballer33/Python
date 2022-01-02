class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_counter = {}

        for number in nums:
            if number in number_counter:
                return True
            else:
                number_counter.setdefault(number, 0)

        return False
