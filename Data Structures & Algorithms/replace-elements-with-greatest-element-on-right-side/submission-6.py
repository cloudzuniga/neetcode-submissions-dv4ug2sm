class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_left = -1
        for i in range(len(arr)-1,-1,-1):
            if max_left<arr[i]:
                max_left,arr[i] = arr[i],max_left
            else:
                arr[i] = max_left
        return arr

