"""
Problem    : 0002. Add Two Numbers
Link       : https://leetcode.com/problems/add-two-numbers/
Difficulty : Medium
Tags       : Linked List, Math, Recursion
Runtime    : 7 ms (beats 24.52%)
Memory     : 19.24 MB (beats 79.75%)
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
