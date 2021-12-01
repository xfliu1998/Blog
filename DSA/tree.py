class Node(object):
    """节点类"""
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, val):
        """为树添加节点"""
        node = Node(val)
        if self.root.val == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃


    def front_recursive(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.val, end=' ')
        self.front_recursive(root.left)
        self.front_recursive(root.right)


    def middle_recursive(self, root):
        """利用递归实现树的中序遍历"""
        if root is None:
            return
        self.middle_recursive(root.left)
        print(root.val, end=' ')
        self.middle_recursive(root.right)


    def later_recursive(self, root):
        """利用递归实现树的后序遍历"""
        if root is None:
            return
        self.later_recursive(root.left)
        self.later_recursive(root.right)
        print(root.val, end=' ')


    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root is None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:               # 从根节点开始，一直找它的左子树
                print(node.val, end=' ')
                myStack.append(node)
                node = node.left
            node = myStack.pop()      # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root is None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:              # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print(node.val, end=' ')
            node = node.right


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root is None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   # 找出后序遍历的逆序存在myStack2里
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:                   # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().val, end=' ')


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        l2 = []
        cur_layer = [root]
        while cur_layer and root:
            l1, next_layer = [], []
            for node in cur_layer:
                l1.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            cur_layer = next_layer
            l2.append(l1)
        return l2


    def morris(self, root, order):
        """实现Morris遍历"""
        if root is None:
            return
        cur = root
        while cur:
            if cur.left is None:
                print(cur.val, end=' ')
                cur = cur.right
            else:
                mostRight = cur.left
                while mostRight.right is not None and mostRight.right != cur:
                    mostRight = mostRight.right
                if mostRight.right is None:
                    mostRight.right = cur
                    # 先序遍历
                    if order == 'front':
                        print(cur.val, end=' ')
                    cur = cur.left
                elif mostRight.right == cur:
                    # 中序遍历
                    if order == 'middle':
                        print(cur.val, end=' ')
                    mostRight.right = None
                    cur = cur.right


if __name__ == '__main__':
    """主函数"""
    vals = range(10)           # 生成十个数据作为树节点
    tree = Tree()
    for val in vals:
        tree.add(val)

    print('队列实现层次遍历:')
    print(tree.level_queue(tree.root))  # [[0], [1, 2], [3, 4, 5, 6], [7, 8, 9]]

    print('\n\n递归实现先序遍历:')
    tree.front_recursive(tree.root)     # 0 1 3 7 8 4 9 2 5 6
    print('\n递归实现中序遍历:')
    tree.middle_recursive(tree.root)    # 7 3 8 1 9 4 0 5 2 6
    print('\n递归实现后序遍历:')
    tree.later_recursive(tree.root)     # 7 8 3 9 4 1 5 6 2 0

    print('\n\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)         # 0 1 3 7 8 4 9 2 5 6
    print('\n堆栈实现中序遍历:')
    tree.middle_stack(tree.root)        # 7 3 8 1 9 4 0 5 2 6
    print('\n堆栈实现后序遍历:')
    tree.later_stack(tree.root)         # 7 8 3 9 4 1 5 6 2 0

    print('\nMorris先序遍历：')
    tree.morris(tree.root, 'front')     # 0 1 3 7 8 4 9 2 5 6
    print('\nMorris中序遍历：')
    tree.morris(tree.root, 'middle')    # 7 3 8 1 9 4 0 5 2 6
