from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [0] * len(nums)
        suffixProd = [0] * len(nums)
        productArr = [0] * len(nums)

        prefixProd[0] = 1
        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]

        suffixProd[-1] = 1
        i = len(nums) - 2
        for n in range(len(nums) - 2, -1, -1):
            suffixProd[i] = nums[n + 1] * suffixProd[n + 1]
            i -= 1

        productArr[0] = suffixProd[0]
        for i in range(1, len(nums)):
            productArr[i] = prefixProd[i] * suffixProd[i] 
        
        return productArr


            
            
