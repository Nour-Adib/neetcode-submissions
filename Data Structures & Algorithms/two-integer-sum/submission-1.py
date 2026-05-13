class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                numbers_sum = nums[i] + nums[j]
                if numbers_sum == target and i != j:
                    return [i, j]

        return []