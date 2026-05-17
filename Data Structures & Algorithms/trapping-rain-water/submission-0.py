class Solution:
    def trap(self, height: List[int]) -> int:
        pointer_a_index = 0
        pointer_b_index = len(height) -1

        volumes = []
        max_a_height = 0
        max_b_height = 0
        for index in range(0, len(height)):
            max_a_height = max(height[pointer_a_index], max_a_height)
            max_b_height = max(height[pointer_b_index], max_b_height)

            if max_a_height < max_b_height:
                volume = max_a_height - height[pointer_a_index]
                pointer_a_index += 1
            else:
                volume = max_b_height - height[pointer_b_index]
                pointer_b_index -= 1

            if volume > 0:
                volumes.append(volume)

        return sum(volumes)
        