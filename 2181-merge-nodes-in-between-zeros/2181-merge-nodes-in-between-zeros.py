# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        temp=dummy
        sum=0

        cur=head.next

        while cur:
            if cur.val==0:
                temp.next=ListNode(sum)
                temp=temp.next
                sum=0
            else:
                sum+=cur.val

            cur=cur.next

        return dummy.next