class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrMap = {}
        i = 0
        for num in nums:
            diff = target - num

            if diff in arrMap:
                return [arrMap[diff], i]
            
            arrMap[num] = i
            i = i + 1 