class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}

        for num in range(len(nums)):
            n = nums[num]
            c = target - n
        
            if c in s:
                return [s[c], num]
            s[n] = num