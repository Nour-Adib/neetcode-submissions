class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointer_a_index = 0
        pointer_b_index = len(numbers) -1

        for _ in range(0, len(numbers)):
            pointer_a_num = numbers[pointer_a_index]
            pointer_b_num = numbers[pointer_b_index]

            nums_sum =  pointer_a_num + pointer_b_num

            if nums_sum > target:
                pointer_b_index -= 1
            elif nums_sum < target:
                pointer_a_index += 1
            else:
                return [pointer_a_index +1 , pointer_b_index +1]
        