class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = [] #变量名别用vars，vars跟查属性的内置函数vars()重复
        A = head
        while A is not None:
            vals.append(A.val)
            A = A.next
        return vals == vals[::-1]
