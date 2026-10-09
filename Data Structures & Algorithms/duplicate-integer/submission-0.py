class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =  set()
        contains_duplicates = False 

        for item in nums: 
            if item not in seen: 
                seen.add(item)
            else:
                contains_duplicates = True

        return contains_duplicates


        