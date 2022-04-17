class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        
        for sentence in sentences:
            spaces_count = sentence.split(" ")
            length = len(spaces_count)
            count = max(count, length)
        return count
    

                    