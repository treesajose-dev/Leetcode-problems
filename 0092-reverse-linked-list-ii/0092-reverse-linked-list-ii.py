# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        co = 1

        temp = head
        prevLeft = None

        # move to left position
        while temp and co < left:
            prevLeft = temp
            temp = temp.next
            co += 1

        curr = temp
        prev = None

        # this becomes tail after reversal
        leftNode = curr

        # reverse from left to right
        while curr and co <= right:

            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

            co += 1

        # connect left part
        if prevLeft:
            prevLeft.next = prev
        else:
            head = prev

        # connect right part
        leftNode.next = curr

        return head