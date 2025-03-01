class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tou,wei = head,None
        while tou is not None:
            mid = tou.next
            tou.next = wei
            wei = tou
            tou = mid
        return wei
