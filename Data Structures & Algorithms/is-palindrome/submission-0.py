import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        pointer_a_index = 0
        pointer_b_index = len(cleaned_string) - 1
        for _ in range(0, len(cleaned_string)//2):
            pointer_a_char = cleaned_string[pointer_a_index]
            pointer_b_char = cleaned_string[pointer_b_index]

            print(f'Char A {pointer_a_char} at index {pointer_a_index}')
            print(f'Char B {pointer_b_char} at index {pointer_b_index}')

            if pointer_a_char != pointer_b_char:
                return False

            pointer_a_index += 1
            pointer_b_index -= 1

        return True

        