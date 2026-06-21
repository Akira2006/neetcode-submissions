class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       seen = {}

       for i in range(len(nums)):
        num = nums[i]

        if num in seen:
            return [seen[num], i]

        need = target - num
        seen[need] = i