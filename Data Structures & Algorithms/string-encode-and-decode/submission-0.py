class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str: str) -> List[str]:
        res, i = [], 0

        while i<len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length]) #le caractère à l'index j+1+length est exclu
            i = j+1+length

        return res