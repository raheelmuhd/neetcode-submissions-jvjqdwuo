class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse_string = []

        for i in range(len(s) - 1, -1, -1):
            reverse_string.append(s[i])
        
        s.clear()

        for i in range(len(reverse_string)):
            s.append(reverse_string[i])

        