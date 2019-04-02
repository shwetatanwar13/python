class Solution(object):
    def arrayRotation(self,l,d):
        for i in range(0,d):
            l.append(l[0])
            l.remove(l[0])
        print(l)

Input=[1, 2, 3, 4, 5, 6, 7]
s=Solution()
s.arrayRotation(Input,2)