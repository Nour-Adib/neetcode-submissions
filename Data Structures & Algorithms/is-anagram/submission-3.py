class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not (len(t) == len(s)):
            return False

        arr_t = list(t)
        for char in s:
            try:
                idx = arr_t.index(char)
                del arr_t[idx]
            except ValueError:
                return False

        return True
        