class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        A = head
        while A is not None:
            vals.append(A.val)
            A = A.next
        return vals == vals[::-1]
