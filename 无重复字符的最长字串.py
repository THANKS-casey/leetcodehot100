class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        i = -1
        # 注意这里不能加while j >= i，因为这样的话这个while条件恒成立，程序会超时的，如果想加，可以在后面的if里再加一个if j >= i
        for j in range(len(s)):

            if s[j] in dic:
                i = max(i,dic[s[j]])
            dic[s[j]] = j
            res = max(res,j-i)
        return res
