# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        values = []
        curr = head 

        while curr:
            values.append(curr.val)
            curr = curr.next
        curr = head 
        for val in reversed(values):
            curr.val = val 
            curr = curr.next
        return head     



        