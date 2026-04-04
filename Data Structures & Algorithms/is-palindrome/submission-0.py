import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res_s = ""
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        res_s = s[::-1]
        if s == res_s:
            return True
        else:
            return False

        