class Solution():
    def firstUniqChar(self, s):
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
obj = Solution()
print(obj.firstUniqChar("leetcode"))      # 0
print(obj.firstUniqChar("loveleetcode"))  # 2
print(obj.firstUniqChar("aabb"))          # -1
