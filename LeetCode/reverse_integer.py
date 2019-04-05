class Solution(object):
    def reverse(self, x):
         x=list(i for i in str(x))
         if x[0]=='-':
            y=int('-'+str(int(''.join(x[len(x)-i] for i in range(1,len(x))))))
         else:
            y=(int((''.join(x[len(x)-i-1] for i in range(0,len(x))))))

         if -2**31<y<2**31-1:
            return(y)
         else:
            return(0)

s=Solution()
print(s.reverse(-123))
