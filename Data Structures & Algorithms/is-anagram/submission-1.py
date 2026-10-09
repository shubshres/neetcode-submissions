class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 

        # Create hashmap for both s and t
        countS, countT = {}, {}

        # loop through the arrays and fill in the hash map with the letters and their counts 
        for i in range(len(s)): 
            # use .get in case key does not exist. 0 is the default value
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # iterate through hash map for both and check if each key/value is the same 
        for c in countS: 
            # if the count is not the same then return false
            if countS[c] != countT.get(c, 0): 
                return False 
        
        # return true saying that each is the same 
        return True