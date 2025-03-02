class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() #这里是未来判断重不重复，所以用集合而不是列表（）
        A = head
        while A is not None:
            if A in seen:
                return True
            seen.add(A) #这里集合加元素是用add 列表加才是用append
            A = A.next
        return False
