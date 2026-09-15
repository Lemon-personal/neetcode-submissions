class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            pre = 1
            prefix = []
            products = []

            for num in nums:
                prefix.append(pre)
                pre *= num

            suf = 1
            n = len(nums)

            for i in range(len(nums)):
                products.append(suf*prefix[n-1-i])
                suf *= nums[(n-1)-i]

            products.reverse()

            return products