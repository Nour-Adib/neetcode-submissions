class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequency = {}

        for index, number in enumerate(nums):
            number_frequency[number] = number_frequency.get(number, 0) + 1 
        
        return sorted(number_frequency, key=number_frequency.get, reverse=True)[:k]
        