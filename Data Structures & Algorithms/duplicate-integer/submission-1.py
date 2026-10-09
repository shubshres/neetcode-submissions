class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        indexed = set()
        contains_duplicates = False 

        for i in nums: 
            if i in indexed:
                contains_duplicates = True 
            else: 
                indexed.add(i)

        return contains_duplicates