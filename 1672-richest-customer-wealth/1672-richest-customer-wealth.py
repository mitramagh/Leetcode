class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        # each_sum = 0
        # each_sum_list=[]
        # for acc in accounts:
        #     for fir_acc in acc:
        #         each_sum += fir_acc
        
        for account in accounts:
            if sum(account)>richest:
                richest = sum(account)
        return richest
            
        