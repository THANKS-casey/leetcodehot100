class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        while A!= B: #其实是判断两个节点是否是一个节点 所以其实就一个A == B的逻辑，而不是A.val == B.val(即除了值相等，还要地址相同)
            A = A.next if A else headB
            B = B.next if B else headA
        return A
