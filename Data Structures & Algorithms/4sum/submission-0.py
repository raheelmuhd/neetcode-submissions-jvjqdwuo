class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        nums.sort()
        for n1 in range(len(nums)):
            if n1 > 0 and nums[n1] == nums[n1 - 1]:
                continue
            for n2 in range(n1 + 1, len(nums)):
                if n2 > n1 + 1 and nums[n2] == nums[n2 - 1]:
                    continue
                left = n2 + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[n1] + nums[n2] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[n1], nums[n2], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        
        return result
                         
        