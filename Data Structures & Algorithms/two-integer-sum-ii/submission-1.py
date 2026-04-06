class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = len(numbers) - 1
        left = 0
        currentsum = 0
        
        while left < right:

            currentsum = numbers[right] + numbers[left]

            if currentsum < target:
                left+=1
            elif currentsum > target:
                right-=1
            else:
                return [left + 1, right + 1] 
        
        