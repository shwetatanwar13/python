class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s1=set()
        for s in emails:
            s = s.split('@')
            s[0]=s[0].replace('.','')
            if '+' in s[0]:
              s[0] = s[0].split('+')
              s[0].pop()
              s1.add(s[0][0] + '@' + s[1])
            else:
              s1.add(s[0] + '@' + s[1])
            print(s)

        print(len(s1))


l=["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]

s=Solution()
s.numUniqueEmails(l)