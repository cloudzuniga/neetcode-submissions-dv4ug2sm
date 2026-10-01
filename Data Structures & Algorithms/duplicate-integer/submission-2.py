class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = list(set(nums))
        print(setNums)
        return True if len(setNums) != len(nums) else False