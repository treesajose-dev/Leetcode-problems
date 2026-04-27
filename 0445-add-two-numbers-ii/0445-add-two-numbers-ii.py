# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        st1=[]
        st2=[]

        while l1:
            st1.append(l1.val)
            l1=l1.next

        while l2:
            st2.append(l2.val)
            l2=l2.next
        
        print(st1)
        print(st2)

        head=None

        carry=0

        while st1 or st2 or carry:
            if st1:
                carry=carry+st1.pop()
            if st2:
                carry=carry+st2.pop()

            node=ListNode(carry%10)
            node.next=head
            head=node

            carry//=10

        return head