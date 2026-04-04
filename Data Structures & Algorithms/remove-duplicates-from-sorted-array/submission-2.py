class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_array = list(set(nums))
        nums.clear()
        for i in unique_array:
            nums.append(i)
        nums.sort()
        k = len(unique_array)
        print(k)
        return k
        