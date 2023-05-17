class Solution(object):
    def subtractProductAndSum(self, n):

        number = str(n)

        product = 1
        for num in number:
            product = product * int(num)

        summ = 0
        for num in number:
            summ = summ + int(num)
        
        result = product - summ

        return result
    
print(Solution.subtractProductAndSum(object,456))