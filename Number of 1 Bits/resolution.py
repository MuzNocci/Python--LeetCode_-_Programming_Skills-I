class Solution(object):
    def hammingWeight(self, n):

        n = str(n)
        sum_one = 0

        for char in n:
            sum_one += int(char)

        return sum_one
    
print(Solution.hammingWeight(Solution, 11111111111111111111111111111101))