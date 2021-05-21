# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        count = 0
        
        while count <= n:
            fast = fast.next
            count += 1
            
        while fast != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
        
        
        