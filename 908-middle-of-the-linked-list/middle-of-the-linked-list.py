# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cnt = 0 
        current = head 
        while current:
            cnt += 1 
            current = current.next  
        # middle part 
        middle = cnt // 2
        current = head

        for i in range(middle):
            current = current.next 
        return current        
        