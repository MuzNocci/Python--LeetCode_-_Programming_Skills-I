class Solution(object):
    def hammingWeight(self, n):

        sum_one = 0

        for i in range(32):

            sum_one += (n & 1)

            n = n >> 1

        return sum_one
    
number = '11111111111111111111111111111101'

print(Solution.hammingWeight(Solution, int(number)))