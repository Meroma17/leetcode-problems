class Solution():
    def isPalindrome(self, x):
        c=str(x)
        if c==c[::-1]:
            return True
        else:
            return False
obj=Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))


        
