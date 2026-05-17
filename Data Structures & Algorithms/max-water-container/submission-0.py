class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer_a_index = 0
        pointer_b_index = len(heights) -1

        max_volume = 0
        while pointer_a_index < pointer_b_index:
            volume = (pointer_b_index - pointer_a_index) * min(heights[pointer_a_index], heights[pointer_b_index])

            if volume > max_volume:
                max_volume = volume

            if heights[pointer_a_index] < heights[pointer_b_index]:
                pointer_a_index += 1
            else:
                pointer_b_index -= 1

        return max_volume
            
            

