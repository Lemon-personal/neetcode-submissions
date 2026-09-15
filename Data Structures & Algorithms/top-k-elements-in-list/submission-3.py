class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numOccurence = {}
        values = []
        for num in nums:
            if num in numOccurence:
                numOccurence[num] += 1
            else:
                numOccurence[num] = 1
        
        tuples = sorted(numOccurence.items(), key=lambda sort: (sort[1], sort[0]))

        for i in range(k):
            values.append(tuples.pop(len(tuples)-1)[0])

        return values