class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        self.equlibrium = None

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
        self.equlibrium_calc()
        self.balance_tree(self)

    def balance_tree(self,tree):
        self.equlibrium_calc()
        
        if self.equlibrium > 1 and self.data < self.left.data:
            Node.rotate_right(tree)
            tree.equlibrium_calc()
        if self.equlibrium < -1 and self.data > self.right.data:
            Node.rotate_left(tree)
            tree.equlibrium_calc()
        # if self.equlibrium > 1 and self.data > self.left.data:
            # Node.rotate_left(tree)
            # Node.rotate_right(tree)
            # tree.equlibrium_calc()
        # if self.equlibrium < -1 and self.data < self.right.data:
            # Node.rotate_right(tree)
            # Node.rotate_left(tree)
            # tree.equlibrium_calc()
            
        if tree.right is not None: 
            self.balance_tree(tree.right)
        if tree.left is not None:
            self.balance_tree(tree.left)

    def equlibrium_calc(self) -> int:
        if self.data is not None:
            self.equlibrium = self.max_depth(self.left) - self.max_depth(self.right)
            if self.left is not None:
                self.left.equlibrium_calc()
            if self.right is not None:
                self.right.equlibrium_calc()

    def rotate_right(self):
        right_node=Node(self.data)
        
        if self.right is not None:
            right_node.right=self.right
        if self.left is not None:
            if self.left.right is not None:
                right_node.left=self.left.right
            self.data=self.left.data
            self.left=self.left.left
        self.right=right_node

    def rotate_left(self):
        left_node=Node(self.data)
        
        if self.left is not None:
            left_node.left=self.left
        if self.right is not None:
            if self.right.left is not None:
                left_node.right=self.right.left
            self.data=self.right.data  
            self.right=self.right.right
        self.left=left_node

    def  print_tree(self,tree, level = 0, prefix = ""):
        if tree.data:
            print(" "*(4*level) + prefix + str(tree.data))
            if tree.left:
                self.print_tree(tree.left, level = level +1, prefix = "L:")
            if tree.right:
                self.print_tree(tree.right, level = level +1, prefix = "R:")

    def in_order_traversal(self, tree):
        result = []
        if tree:
            result = self.in_order_traversal(tree.left)
            result.append(tree.data)
            result.extend(self.in_order_traversal(tree.right))
        return result

    def max_depth(self, tree, depth=0):
        if tree is None:
            return depth-1
        return max(self.max_depth(tree.left, depth=depth +1),
                   self.max_depth(tree.right, depth=depth +1))

    def contains(self,tree, data):
        if tree:
            if tree.data == data:
                return True
            if tree.data < data:
                return self.contains(tree.right, data)
            if tree.data > data:
                return self.contains(tree.left, data)
        return False

tree = Node()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.print_tree(tree)

print(tree.in_order_traversal(tree))
assert tree.in_order_traversal(tree) == [1, 2, 3, 4, 5, 6, 7]
assert tree.contains(tree, 3)
assert not tree.contains(tree, 20)
assert tree.max_depth(tree) <= 2

tree = Node()

tree.insert(2)
tree.insert(10)
tree.insert(3)
tree.insert(5)
tree.insert(100)

assert tree.max_depth(tree) <= 2