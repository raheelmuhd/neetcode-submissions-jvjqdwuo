class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1 = 0
        w2 = 0
        l = 0
        string_output = ""
        while min(w1, w2) < min(len(word1), len(word2)):
            if l % 2 == 0:
                string_output += word1[w1]
                w1 += 1
            if l % 2 != 0:
                string_output += word2[w2]
                w2 += 1
            l+=1

        if len(word1) > len(word2):
            for i in range(w1, len(word1)):
                string_output += word1[i]
        if len(word2) > len(word1):
            for i in range(w2,len(word2)):
                string_output += word2[i]
        
        return string_output

        