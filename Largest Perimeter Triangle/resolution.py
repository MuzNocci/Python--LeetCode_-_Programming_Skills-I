class Solution(object):
    def largestPerimeter(self, nums):

        if len(nums) != 3:
            return 0
        else:
            return sum(nums)
        
print(Solution.largestPerimeter(Solution , '[3,2,3,4]'))