class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: #主框架 中间的处理过程塞到了一个自定义的函数dfs里
        res = []  
        self.dfs(root, res)
        return res

    def dfs(self, node: Optional[TreeNode], res: List[int]) -> None:
        if not node: # 递归，启动！
            return # 递归的终止条件 return空相当于停止
        self.dfs(node.left, res)    # 先处理左子树
        res.append(node.val)         # 再处理当前节点
        self.dfs(node.right, res)    # 最后处理右子树

'''

    3
   / \
  9   2


如果我们把 `res.append(node.val)` 放在不同位置，会得到不同的遍历顺序：

1. 如果放在最前面（前序遍历）：

res.append(node.val)         # 先处理当前节点
self.dfs(node.left, res)    # 再处理左子树
self.dfs(node.right, res)   # 最后处理右子树

结果会是：[3,9,2]（根->左->右）

2. 如果放在中间（中序遍历）：

self.dfs(node.left, res)    # 先处理左子树
res.append(node.val)         # 再处理当前节点
self.dfs(node.right, res)   # 最后处理右子树

结果会是：[9,3,2]（左->根->右）

3. 如果放在最后（后序遍历）：

self.dfs(node.left, res)    # 先处理左子树
self.dfs(node.right, res)   # 再处理右子树
res.append(node.val)         # 最后处理当前节点

结果会是：[9,2,3]（左->右->根）

所以，为了实现中序遍历（左->中->右），我们必须把 `res.append(node.val)` 放在处理完左子树之后，处理右子树之前。
'''
