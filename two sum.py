class Solution(object):
    def twoSum(self, nums, target):
        nm={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in nm:
                return [nm[comp],i]
            nm[num]=i
