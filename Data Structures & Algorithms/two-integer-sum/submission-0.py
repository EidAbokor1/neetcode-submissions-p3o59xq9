class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_index = {}
        
        for num in range(len(nums)):
            n = nums[num]
            c = target - n
            
            if c in num_index:
                return [num_index[c], num]
            num_index[n] = num

