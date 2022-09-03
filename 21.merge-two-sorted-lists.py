"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
from typing import Optional
#TODO to be complete
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __str__(self):
    #     s = f"({str(self.val)})"
    #     if self.next:
    #         s += f" -> {self.next}"  # be careful not to build any circular lists...
    #     return s


class Solution:
    def mergeTwoLists(self,l1, l2) -> ListNode:
        # Check if either of the lists is null
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # Choose head which is smaller of the two lists
        if (l1.val) < (l2.val):
            temp = head = ListNode(l1)
            l1 = l1.next
        else:
            temp = head = ListNode(l2)
            l2 = l2.next
        # Loop until any of the list becomes null
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        # Add all the nodes in l1, if remaining
        while l1 is not None:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next
        # Add all the nodes in l2, if remaining
        while l2 is not None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next
        # print(l2.val)
        return head

    # def mergeTwoLists(self, list1_: Optional[ListNode], list2_: Optional[ListNode]):
    #     # -> Optional[ListNode]:
    #     place_holder = ListNode()
    #     list1 = ListNode(list1_)
    #     list2 = ListNode(list2_)
    #     temp = place_holder

    #     position = dummyHead = ListNode()
    #     while list1 is not None and list2 is not None:
    #         if (list1_.val) <= (list2_.val):
    #             position.next = list1
    #             list1 = list1.next
    #             # breakpoint()
    #         else:
    #             position.next = list2
    #             list2 = list2.next
    #         position = position.next

    #     # merge residual list1
    #     if list1 is None:
    #         position.next = list
    #     # merge residual list2
    #     if list2 is None:
    #         position.next = list1

    #     breakpoint()
    #     # print(dummyHead.val)
    #     return dummyHead.next


if __name__ == "__main__":
    s = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    list1 = ListNode(l1)
    list2 = ListNode(l2)
    print(s.mergeTwoLists(list1, list2))
