from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = []

        prefixes = [1 for _ in range(0, len(nums))]
        suffixes = [1 for _ in range(0, len(nums))]

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            products.append(prefixes[i] * suffixes[i])

        return products 

        