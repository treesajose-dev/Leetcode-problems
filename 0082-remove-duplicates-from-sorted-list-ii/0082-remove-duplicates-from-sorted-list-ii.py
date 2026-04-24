# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        dict1 = {}
        temp = head   

        # count frequency
        while temp:
            if temp.val not in dict1:
                dict1[temp.val] = 1
            else:
                dict1[temp.val] += 1
            temp = temp.next

        stack = []
        temp = head   

        # collect values with count == 1
        while temp:
            if dict1[temp.val] == 1:
                stack.append(temp.val)
            temp = temp.next

        # build linked list
        dummy = ListNode(0)
        current = dummy

        for item in stack:
            current.next = ListNode(item)
            current = current.next

        return dummy.next
