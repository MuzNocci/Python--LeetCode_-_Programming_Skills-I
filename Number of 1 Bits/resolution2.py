class Solution(object):
    def hammingWeight(self, n):

        return len(str(n).replace('0',''))
    
number = '11111111111111111111111111111101'

print(Solution.hammingWeight(Solution, int(number)))