class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        uniquenum = set()

        for num in nums:
            uniquenum.add(num)
        
        if len(uniquenum) == len(nums):
            return False
        else:
            return True