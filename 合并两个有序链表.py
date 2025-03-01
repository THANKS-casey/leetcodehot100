class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val: # 意味着我们确定了合并后的链表当前节点是 l1 （因为它的值较小）
            l1.next = self.mergeTwoLists(l1.next,l2) # 让当前 l1 节点指向合并后的新链表（其实就是更新 l1 当前节点的 next 指针，使其指向后续正确的节点）；可以认为，l1.next = self.mergeTwoLists(l1.next,l2)这里既是更新了l1链表，也更新了l1.next链表
            return l1 # 因为这里的递归更新的是l1，所以当然返回是返回l1了
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
