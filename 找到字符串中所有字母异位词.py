class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt_p = Counter(p) # p的标准答案
        cnt_s = Counter() # s的可变对象，用于与p的标准答案对比
        for right,c in enumerate(s): # 遍历右指针，也就是滑窗的右端
            cnt_s[c] += 1 # 因为右指针是从0索引开始的，所以相当于遍历完整个字符串，所以顺便在这里把记录的字符数存在之前创建的cnt_s可变变量里
            left = right - len(p) + 1 # 定滑窗左端的索引位置（后面也是要输出索引left的）
            if left < 0: # 滑窗长度不够，继续动右指针
                continue
            if cnt_s == cnt_p: # 判定，已记录的滑窗内和标准答案一样
                ans.append(left) # 答案索引记上
            cnt_s[s[left]] -= 1 # 因为滑窗长度是定的，所以在进入下一个右索引之前，当前左端位置这个字符就要从变量cnt_s里丢掉
        return ans
