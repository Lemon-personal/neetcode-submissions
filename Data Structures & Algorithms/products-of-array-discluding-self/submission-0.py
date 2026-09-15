class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            pre = 1
            prefix = []
            products = []

            for num in nums:
                prefix.append(pre)
                pre *= num

            suf = 1
            suffix = []
            n = len(nums)

            for i in range(len(nums)):
                suffix.append(suf)
                suf *= nums[(n-1)-i]
        
            for i in range(len(suffix)):
                products.append(suffix[n-1-i]*prefix[i])

            return products