class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s=""
        if s==" " or len(s)==1:
            return True
        for str in s:
            if str.isalpha() or str.isdigit():
                filtered_s+=str.lower()
        if filtered_s==filtered_s[::-1]:
            return True
        elif filtered_s==" ":
            return True
    
        return False