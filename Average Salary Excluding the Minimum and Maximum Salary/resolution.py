class Solution(object):
    def average(self, salary):

        salary.remove(min(salary))
        salary.remove(max(salary))

        sum_salary = float(sum(salary))

        return sum_salary / len(salary)
    
print(Solution.average(Solution, [1000,2000,3000]))