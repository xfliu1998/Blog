import queue

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.elem,)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem,)
        self.middle_digui(root.rchild)


    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem,)


    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print(node.elem,)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild                  #开始查看它的右子树


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.elem,)
            node = node.rchild                  #开始查看它的右子树


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().elem,)


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem,)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

    def levelOrder(self,root):
        """BFS层次"""
        res = []
        if root == None:
            return res

        q = [root]
        while len(q) != 0:
            res.append([node.elem for node in q])
            new_q = []
            for node in q:
                if node.lchild:
                    new_q.append(node.lchild)
                if node.rchild:
                    new_q.append(node.rchild)
            q = new_q

        return res



    def treeDepth(self,tree):
        if tree == None:
            return 0
        leftDepth = self.treeDepth(tree.lchild)
        rightDepth = self.treeDepth(tree.rchild)
        if leftDepth > rightDepth:
            return leftDepth + 1
        if rightDepth >= leftDepth:
            return rightDepth + 1

    def button_up_maxDepth(self, root):
        if root == None:
            return 0
        leftmax = self.button_up_maxDepth(root.lchild)
        rightmax = self.button_up_maxDepth(root.rchild)
        return max(leftmax, rightmax) + 1

    answer = 0
    def top_down_maxDepth(self, root,deepth):
        if root == None:
            return
        if root.lchild == None and root.rchild == None:
            self.answer= max(self.answer,deepth)
            #print(self.answer)

        self.top_down_maxDepth(root.lchild,deepth+1)
        self.top_down_maxDepth(root.rchild,deepth+1)


    def treeWidth(self,tree):
        curwidth = 1
        maxwidth = 0
        q = queue.Queue()
        q.put(tree)
        while not q.empty():
            n = curwidth
            for i in range(n):
                tmp = q.get()
                curwidth -= 1
                if tmp.rchild:
                    q.put(tmp.lchild)
                    curwidth += 1
                if tmp.rchild:
                    q.put(tmp.rchild)
                    curwidth += 1
            if curwidth > maxwidth:
                maxwidth = curwidth
        return maxwidth

    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.elem == q.elem:
            return self.help(p.rchild, q.lchild) and self.help(p.lchild, q.rchild)#递归判断左子树根的右子树根节点和右子树根的左子树根节点以及左子树根的左子树根节点和右子树根的右子树根节点的值是否相等
        return False

    def isSymmetric(self, root):
        if root:
            return self.help(root.lchild, root.rchild)
        return True

    def hasPathSum(self, root, sum: int):
        if root == None:
            return False
        if root.lchild == None and root.rchild == None:
            return root.elem == sum
        return self.hasPathSum(root.lchild,sum - root.elem) or self.hasPathSum(root.rchild, sum - root.elem)




if __name__ == '__main__':
    """主函数"""
    elems = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for elem in elems:
        tree.add(elem)           #逐个添加树的节点

    print('队列实现层次遍历:')
    tree.level_queue(tree.root)

    print('\n\n递归实现先序遍历:')
    tree.front_digui(tree.root)
    print('\n递归实现中序遍历:')
    tree.middle_digui(tree.root)
    print('\n递归实现后序遍历:')
    tree.later_digui(tree.root)

    print('\n\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)
    print('\n堆栈实现中序遍历:')
    tree.middle_stack(tree.root)
    print('\n堆栈实现后序遍历:')
    tree.later_stack(tree.root)
    print('\n堆栈深度:')
    print(tree.treeDepth(tree.root))
    print('\n堆栈宽度:')
    print(tree.treeWidth(tree.root))
    print('\n堆栈分层排序:')
    print(tree.levelOrder(tree.root))
    print('\nbutton up堆栈深度:')
    print(tree.button_up_maxDepth(tree.root))

    print('\ntop down堆栈深度:')
    tree.top_down_maxDepth(tree.root,1)
    print(tree.answer)

    print('\n是否有path sum等于11:')
    print(tree.hasPathSum(tree.root,8))


    elems2 = [1, 2, 2, 3, 4, 4, 3]
    tree2 = Tree()  # 新建一个树对象
    for elem in elems2:
        tree2.add(elem)  # 逐个添加树的节点
    print('\n堆栈分层排序:')
    print(tree2.levelOrder(tree2.root))
    print('\n是否是堆成二叉树:')
    print(tree2.isSymmetric(tree2.root))


