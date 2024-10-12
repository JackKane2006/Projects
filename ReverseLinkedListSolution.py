# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.newHead = None
    
    def reverseList(self, head):
        if head == None: 
            return None
        self.reverseListHelper(head)
        head.next = None
        return self.newHead

    def reverseListHelper(self, head):
        prev = head.next 
        if prev != None:
            self.reverseListHelper(head.next)
            prev.next = head
        else:
            self.newHead = head
    
