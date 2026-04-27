# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        stack=[]
        temp=head

        while temp:
            stack.append(temp.val)
            temp=temp.next

        m=len(stack)-n
        co=0

        if m==0:
            return head.next

        temp=head
        while co<m-1:
            temp=temp.next
            co+=1

        temp.next=temp.next.next

        return head
        
        

        
