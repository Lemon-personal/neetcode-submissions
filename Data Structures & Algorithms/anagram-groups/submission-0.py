class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}


        for s in strs:
            alphCounter = []

            for i in range(len(s)):
                alphCounter.append(s[i])
        
            sortedWord = "".join(sorted(alphCounter))
            if sortedWord in anagramDict:
                anagramDict[sortedWord].append(s)
            else:
                anagramDict[sortedWord] = []
                anagramDict[sortedWord].append(s)

        return list(anagramDict.values())