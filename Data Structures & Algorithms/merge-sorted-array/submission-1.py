class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        count = 0
        for i in reversed(nums1):
            if count == len(nums2):
                break
            nums1.remove(i)
            count += 1

        for i in nums2:
            nums1.append(i)
        
        nums1.sort()
        