import re #regular expression
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        res_s = s[::-1]
        if res_s == s:
            return True
        else:
            return False



        