# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        new_list = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                new_list.next = l1
                l1 =l1.next
            else:
                new_list.next = l2
                l2=l2.next
            new_list = new_list.next

        if l1:
            new_list.next = l1

        else:
            new_list.next = l2
        return dummy.next


l1 = ListNode(1,ListNode(2,ListNode(3,None)))
l2 = ListNode(1,ListNode(3,ListNode(4,None)))
print(Solution().mergeTwoLists(l1,l2).next.val)