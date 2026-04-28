class Solution():
    def singleNumber(self,nums):
        d = {}
        for c in nums:
            d[c]=d.get(c, 0) + 1
        for i, c in enumerate(nums):
            if d[c]==1:
                return c
obj = Solution()
print(obj.singleNumber([2,2,1]))
print(obj.singleNumber([4,1,2,1,2]))
print(obj.singleNumber([1]))
