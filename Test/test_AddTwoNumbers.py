# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import sys, os
sys.path.append(os.path.join("..", "Solutions"))
sys.path.append(os.path.join("Solutions"))

from AddTwoNumbers import Solution

solution = Solution()

def test_AddTwoNumbers_1():
    assert solution.addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))), 
        ListNode(5, ListNode(6, ListNode(4))),
        ) == ListNode(7, ListNode(0, ListNode(8)))