class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num_list=[]
        for op in operations:
            if op == "X++"or op == "++X":
                num_list.append(1)
            elif op == "--X" or op == "X--":             
                num_list.append(-1)
                
        return sum(num_list)
        