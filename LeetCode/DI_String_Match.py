class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l=list(range(0,len(S)))
        print(l)
        cont=True
        while cont:
           for i in range(0,len(S)+1):
               if i=='I':
                   if l[i]>l[i+1]:
                       l[i],l[i+1]=l[i+1],l[i]
               elif i=='D':
                   if l[i]<l[i+1]:
                       l[i],l[i+1]=l[i+1],l[i]




Input="IDID"
s=Solution()
s.diStringMatch(Input)
