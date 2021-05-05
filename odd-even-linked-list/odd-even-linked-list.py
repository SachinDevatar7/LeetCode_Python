# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        
        odd = head
        even = head.next
        
       # hodd = head 
        heven = head.next
        
        if head == None or head.next == None:
            return head
        
        
        while even and even.next:
            odd.next = even.next            
            odd = odd.next
            even.next = odd.next
            even = even.next
            
            
        
        odd.next = heven
          
        return dummy.next
        