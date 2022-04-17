class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        
#         for account in accounts:
#             if sum(account)>richest:
#                 richest = sum(account)
#         return richest
            
        
        max_num = max([sum(account) for account in accounts])
        return max_num