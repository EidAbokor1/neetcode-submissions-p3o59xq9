class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        var1 = {}
        var2 = {}

        for var in range(len(s)):
            a = s[var]
            
            if a in var1:
                var1[a] += 1
            else:
                var1[a] = 1
        
        for var in range(len(t)):
            b = t[var]
            
            if b in var2:
                var2[b] += 1
            else:
                var2[b] = 1
        
        if var1 == var2:
            return True
        else:
            return False

            