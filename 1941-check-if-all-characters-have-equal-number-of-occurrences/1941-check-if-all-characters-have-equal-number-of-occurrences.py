class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for str in s:
            if str not in freq:
                freq[str]=1
            else:
                freq[str]+=1
                
        count=freq[s[0]]
        for str in s:
            if freq[str]!=count:
                return False
        return True
                