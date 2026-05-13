class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()

        return s_list == t_list
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        combined_list = []
        anagram_map = {}

        for i in range(len(strs)):
            interm_list = []
            interm_list.append(strs[i])
            for j in range(i+1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    interm_list.append(strs[j])

            if anagram_map.get(strs[i]):
                continue

            for item in interm_list:
                anagram_map[item] = interm_list
            combined_list.append(interm_list)
            

        return combined_list