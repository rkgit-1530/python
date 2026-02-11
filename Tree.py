class TreeNode:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

class Tree:
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
    
    def height(self,root):
        if root is None:
            return 0
        else:
            lheight=self.height(root.left)
            rheight=self.height(root.right)
            h=max(lheight,rheight)+1
            return h
    def diameter(self,root):
        if root is None:
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        ldiameter=self.diameter(root.left)
        rdiameter=self.diameter(root.right)
        diameter=max(lheight+rheight+1,max(ldiameter,rdiameter))
        return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left=TreeNode(4)
root.right.right=TreeNode(5)
root.left.right=TreeNode(6)
t=Tree()
print("Inorder Traversal")
t.inorder(root)
print("\nPreorder Traversal")
t.preorder(root)
print("\nPostorder Traversal")
t.postorder(root)
print("\nHeight of the tree is",t.height(root))
print("Diameter of the tree is",t.diameter(root))

