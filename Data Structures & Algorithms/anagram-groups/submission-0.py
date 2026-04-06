class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for word in strs:
            sort_word = ''.join(sorted(word))
        
            if sort_word not in res:
                res[sort_word]=[]
            res[sort_word].append(word)
            
        return list(res.values())
