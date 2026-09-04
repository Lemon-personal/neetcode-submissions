class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check:List[int] = []

        for num in nums:
            if num not in check:
                check.append(num)

        if len(check) == len(nums):
            return False
    
        return True