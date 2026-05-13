from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        nums_counter = Counter(nums)
        most_common_number = nums_counter.most_common(1)

        number_of_occurences = most_common_number[0][1]

        if number_of_occurences > 1:
            return True

        return False
        