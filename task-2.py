1.  Question 
class Solution:
    def runningSum(self, nums):
        result = []
        total = 0
        
        for n in nums:
            total += n
            result.append(total)
        
        return result
 obj = Solution()
nums = [1, 2, 3, 4]
output = obj.runningSum(nums)
print(output)

2.Question
class Solution:
    def shuffle(self, nums,n): 
        result = []
        for i in range(n):
            result.append(nums[i])       
            result.append(nums[i + n])  
        
        return result
obj = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
output = obj.shuffle(nums,n)
print(output)

3.  Question
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candies = max(candies)   
        for c in candies:
            result.append(c + extraCandies >= max_candies)
        return result
obj = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
output = obj.kidsWithCandies(candies, extraCandies)
print(output)
