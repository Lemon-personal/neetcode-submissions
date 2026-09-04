class Solution:
    def isPalindrome(self, s: str) -> bool:
        remChars = "!@#$%^&*()_+~<>?:{}|`-=/.,';\][ "
        table = s.maketrans(s,s,remChars)
        s = s.translate(table).lower()

        for i in range(len(s)):
            if s[i] != s[(len(s)-1)-i]:
                return False


        return True