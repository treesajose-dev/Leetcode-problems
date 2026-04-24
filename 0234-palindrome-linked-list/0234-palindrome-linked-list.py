# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        new_lis=[]
        while head:
            new_lis.append(head.val)
            head=head.next

        return new_lis==new_lis[::-1]
        

        