class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}


        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord in anagramDict:
                anagramDict[sortedWord].append(s)
            else:
                anagramDict[sortedWord] = []
                anagramDict[sortedWord].append(s)

        return list(anagramDict.values())