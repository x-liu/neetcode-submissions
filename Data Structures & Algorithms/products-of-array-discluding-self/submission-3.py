class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nZeros = 0
        maxNum = 1
        for num in nums:
            if num == 0:
                nZeros+=1
            else:
                maxNum*=num
        out = [0] *len(nums)
        if nZeros == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    out[i] = maxNum
                    return out
        if nZeros == 0:
            for i, num in enumerate(nums):
                out[i] = maxNum//num
        return out




