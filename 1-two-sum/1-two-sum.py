class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,num in enumerate(nums):
            if num not in dict:
                dict[num]=i
            remain=target-num
            if remain in dict and i !=dict[remain]:
                    return [ i, dict[remain]]
                
                
#              D = {}
#         for i,n in enumerate(N):
#             if n not in D: D[n] = i
#             x = t - n
#             if x in D and D[x] != i: return [i,D[x]]

                