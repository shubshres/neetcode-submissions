class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ranthrough = set()
        contains_duplicates = False 

        for i in nums: 
            if i not in ranthrough: 
                ranthrough.add(i)
            else: 
                contains_duplicates = True

        return contains_duplicates