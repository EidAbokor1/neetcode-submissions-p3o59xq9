class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = []
        j = []

        for num in range(len(nums)):
            i = nums[num]
            for num2 in range(len(nums)):
                j = nums[num2]

                if num != num2:
                    if i + j == target:
                        return [num,num2]