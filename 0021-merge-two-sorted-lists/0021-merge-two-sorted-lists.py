# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        new_lis1 = []
        new_lis2 = []
        merge_lis = []

        while list1:
            new_lis1.append(list1.val)
            list1 = list1.next
        
        while list2:
            new_lis2.append(list2.val)
            list2 = list2.next   

        m = len(new_lis1) 
        n = len(new_lis2)

        i = 0
        j = 0

        # merge two sorted lists
        while i < m and j < n:
            if new_lis1[i] < new_lis2[j]:
                merge_lis.append(new_lis1[i])
                i += 1
            else:
                merge_lis.append(new_lis2[j])
                j += 1

        # remaining elements
        while i < m:
            merge_lis.append(new_lis1[i])
            i += 1
        
        while j < n:
            merge_lis.append(new_lis2[j])
            j += 1

        # convert list → linked list
        dummy = ListNode(0)
        current = dummy

        for val in merge_lis:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

        for val in merge_lis:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

