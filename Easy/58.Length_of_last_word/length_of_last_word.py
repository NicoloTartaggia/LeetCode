class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        currWordLen = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if currWordLen > 0:
                    return currWordLen
            else:
                if i == 0:
                    return currWordLen+1
                else:
                    currWordLen += 1