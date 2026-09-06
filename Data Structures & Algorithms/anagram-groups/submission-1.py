class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        var = {}

        for n in range(len(strs)):
            s = "".join(sorted(strs[n]))

            if s in var:
                var[s].append(strs[n])      
            else:
                var[s] = [strs[n]]   
            
        return list(var.values())
            
