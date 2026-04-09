class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        buffer = []
        ones = 0
        for x in nums:
            if x == 0:
                buffer.append(ones)
                ones = 0
            else:
                ones += 1
        buffer.append(ones)
        return max(buffer)


        