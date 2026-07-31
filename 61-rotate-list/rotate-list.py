# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head 
        # find lenght 
        len = 0
        curr = head 

        while curr:
            len += 1
            curr = curr.next
        k %= len

        for _ in range(k):
            prev = None 
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next  
            prev.next = None 
            curr.next = head

            head = curr 
        return head              


        