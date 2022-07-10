class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range(lowLimit,highLimit+1):
            sum = 0
            for s in str(i):
                sum += int(s)
            if sum not in d:
                d[sum] = [i]
            else:
                d[sum].append(i)
        print(d)
        return max(len(n) for n in d.values())