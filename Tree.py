class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None


    def insert(self,root,key):
        if root is None:
             return TreeNode(key)
        else:
            if root.val<key:
                root.right=self.insert(root.right,key)
            else:
                root.left=self.insert(root.left,key)
        return root

    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val,end=" ")
            self.inorder_traversal(root.right)

    def search(self,root,key):
        if root is None or root.val==key:
            return root
        if root.val<key:
            return self.search(root.right,key)
        return self.search(root.left,key)
bst=BST()
bst.root=bst.insert(bst.root,50)
bst.insert(bst.root,30)
bst.insert(bst.root,20)
bst.insert(bst.root,40)
bst.insert(bst.root,70)
bst.insert(bst.root,60)


print('inorder :')
bst.inorder_traversal(bst.root)
print()
