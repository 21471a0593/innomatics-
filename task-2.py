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

