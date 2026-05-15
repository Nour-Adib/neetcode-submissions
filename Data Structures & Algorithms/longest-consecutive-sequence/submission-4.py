class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Deduplicate
        numbers_set = list(set(nums))
        numbers_set.sort()
        max_length_seen = 0

        for index in range(0, len(numbers_set)):
            print(index)

            current_number  = numbers_set[index]
            target = current_number -1

            if target in numbers_set:
                continue
            
            # If we are here that means the current_number is the start of a set
            local_maximum = 1
            larger_number_exists = True
            next_in_sequence = current_number
            while larger_number_exists:
                next_in_sequence +=1 
                if next_in_sequence in numbers_set:
                    local_maximum += 1
                    continue
                larger_number_exists = False

            max_length_seen = local_maximum if local_maximum > max_length_seen else max_length_seen
                
            print("_________")

        
        return max_length_seen