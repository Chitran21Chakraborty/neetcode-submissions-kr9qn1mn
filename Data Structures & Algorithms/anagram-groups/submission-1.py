from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            lst = [0] * 26
            for char in s:
                lst[ord(char) - ord('a')] += 1
            lst = tuple(lst)
            dic[lst].append(s)
        return list(dic.values())
        