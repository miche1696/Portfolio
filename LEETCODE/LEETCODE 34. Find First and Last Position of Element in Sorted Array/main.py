class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        toRet = [-1,-1] 
        try:
            toRet[0] = nums.index(target)
            toRet[1] = toRet[0]
            l = len(nums)
            while (toRet[1]+1<l and nums[toRet[1]+1]==target):
                toRet[1]=toRet[1]+1
            return toRet
        except ValueError:
            return [-1,-1]
        
        return [-1,-1]