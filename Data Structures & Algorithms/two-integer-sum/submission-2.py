class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_map = {}

        for index, value in enumerate(nums):
            diff_from_value = target - value

            potential_index = values_map.get(diff_from_value, -1)
            if potential_index > -1:
                return [potential_index, index]

            values_map[value] = index
            

        return []