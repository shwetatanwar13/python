# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
       count = 0
       num1  = 0
       num2  = 0
       while l1:
         num1 = num1 + l1.val*10**count
         count = count +1
         l1 = l1.next

       count = 0
       while l2:
           num2 = num2 + l2.val * 10 ** count
           count = count + 1
           l2 = l2.next

       print(num1)
       print(num2)
       q= (num1+num2)
       print(q)
       if q==0:
           return ListNode(0, None)
       counter = 0
       while q != 0:
           rem = q%10
           q   = q//10
           if counter == 0:
               newList = ListNode(rem,None)
               head = newList
               print(newList.val)
           else:
               l = ListNode(rem,None)
               newList.next = l
               newList = newList.next
           counter = counter+1
       return head



l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,None)))))))
l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,None))))
#l1 = ListNode(2,ListNode(4,ListNode(3,None)))
#l2 = ListNode(5,ListNode(6,ListNode(4,None)))

print(Solution().addTwoNumbers(l1, l2).val)