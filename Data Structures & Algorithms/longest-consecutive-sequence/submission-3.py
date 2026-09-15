class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = sorted(nums)
        maxCounter = 0
        if len(nums) > 0:
            maxCounter += 1
        else:
            return maxCounter

        print(numSet)

        counter = 1
        for i in range(1,len(numSet)):
            if numSet[i] == numSet[i-1]+1:
                counter += 1
            elif numSet[i] == numSet[i-1]:
                counter = counter
            else:
                maxCounter = max(counter,maxCounter)
                counter = 1
                
        maxCounter = max(counter,maxCounter)

        return maxCounter 