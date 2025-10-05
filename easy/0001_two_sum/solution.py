from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in targets:
                return [targets[diff], i]
            else:
                targets[nums[i]] = i
            
       
        
test = Solution()

print(test.twoSum([2, 7, 11, 15], 9))
        
