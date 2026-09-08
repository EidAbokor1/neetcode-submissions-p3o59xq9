class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in range(len(nums)):
            if nums[num] in dic:
                dic[nums[num]]+= 1
            else:
                dic[nums[num]] = 1
            
        ordered=sorted(dic.items(), key=lambda x: x[1], reverse=True)

        result = []

        i = 0 
        while i < k:
            result.append(ordered[i][0])
            i += 1
        return result
