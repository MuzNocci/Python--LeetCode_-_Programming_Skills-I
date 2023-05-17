class Solution(object):
    def countOdds(self, low, high):

        counter = 0
        
        for n in range(low, high+1):
            print(n)
            if (n % 2) == 1:
                counter += 1
        
        return counter
            
print(Solution.countOdds(Solution, 3, 7))