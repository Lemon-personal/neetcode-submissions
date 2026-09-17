class Solution:

    def encode(self, strs: List[str]) -> str:
        encd = []
        for s in strs:
            encd.append(f"{len(s)},")
        
        encd.append('#')

        combinedString = "".join(strs)
        encd.append(combinedString)

        return "".join(encd)


    def decode(self, s: str) -> List[str]:
        decode = []
        splitStr = s.split("#",1)
        nums = splitStr[0].split(",")
        encdString = splitStr[1]

        charCounter = 0
        for i in range(len(nums)-1):
            word = []
            for j in range(int(nums[i])):
                word.append(encdString[charCounter])
                charCounter += 1
            decode.append("".join(word))   
        
        return decode