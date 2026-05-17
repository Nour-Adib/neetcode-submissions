class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        responses = set()

        for index in range(0, len(nums)):
            target = -nums[index]

            pointer_a_index = index + 1
            pointer_b_index = len(nums) -1

            while pointer_a_index < pointer_b_index:
                pointer_a_num = nums[pointer_a_index]
                pointer_b_num = nums[pointer_b_index]

                num_sum = pointer_a_num + pointer_b_num

                if num_sum > target:
                    pointer_b_index -= 1
                elif num_sum < target:
                    pointer_a_index += 1
                else:
                    responses.add((nums[index], pointer_a_num, pointer_b_num))
                    pointer_b_index -= 1
                    pointer_a_index += 1



        return list(responses)
        