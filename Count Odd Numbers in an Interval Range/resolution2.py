class Solution(object):
    def countOdds(self, low, high):

        counter = []
        
        for n in range(low, high+1):
            if (n % 2) == 1:
                counter.append(n)
        
        return len(counter)
    
print(Solution.countOdds(object, 500, 11000))