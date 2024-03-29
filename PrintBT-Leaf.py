class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def PrintLeafLeftToRight(root):
    s1 = []
    s2 = []
    s1.append(root)
    while len(s1) != 0:
        curr = s1.pop()
        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)
        elif not curr.left and not curr.right:
            s2.append(curr)
    while len(s2) != 0:
        print(s2.pop().data, end=" ")
#      6
#   4      8
# 3   5   7   9
root = node(6)
root.left = node(4)
root.left.left = node(3)
root.left.right = node(5)
root.right = node(8)
root.right.left = node(7)
root.right.right = node(9)
PrintLeafLeftToRight(root)
