class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for num in range(len(nums)):
            i = nums[num]
            j = target - i

            if j in seen:
                return [seen[j], num]
            else:
                seen[i] = num
            

