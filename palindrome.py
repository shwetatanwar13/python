class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag=True
        count=(len(str(x))//2)
        x=str(x)
        print(count)
        for i in range(0,count):
            if x[i]!=x[len(x)-1-i]:
                flag=False
                break
        print("Palindrome" if flag else "not a palindrome")

Solution().isPalindrome(1211)