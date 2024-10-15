#Leetcode medium difficulty problem: https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
       
#Solution
class Solution(object):
    def __init__(self):
        self.newHead = None
        self.nums = []
    
    def addTwoNumbers(self, l1, l2): #solution
        l1Num = self.getNum(l1)
        l2Num = self.getNum(l2)
        numbers = list(str(l1Num + l2Num))
        newListHead = self.numsToLinkedList(numbers)
        return newListHead

    def getNum(self, head): #converts a linked list to a reversed integer ([1, 2, 3] becomes 321)
        if head == None:
            return 0
        else:
            return head.val + 10 * self.getNum(head.next)

    def numsToLinkedList(self, nums): #converts an array of numbers to a reversed linked list
        if nums == []:
            return None
        listHead = ListNode(int(nums[len(nums) - 1]), None)
        curr = listHead
        for i in range(1, len(nums)):
            curr.next = ListNode(int(nums[len(nums) - i - 1]), None)
            curr = curr.next
        return listHead
        
        
