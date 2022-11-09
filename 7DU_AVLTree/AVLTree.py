class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, tree, data):
        if self.data is not None:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
            
        self.level_tree()
    def level_tree(self,tree):
        if self.balance<=-2:
            Node.left_rotation(tree)
        if self.balance >= 2:
            Node.right_rotation(tree)

            
        if tree.right is not None: 
            self.balance(tree.right)
        if tree.left is not None:
            self.balance(tree.left)
    
    def right_rotation(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3
        return y

    def left_rotation(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2
        return y

    def balance(self) => bool, int:
        left_depth = self.max_depth(self.left)
        right_depth = self.max_depth(self.right)
        return left_depth - right_depth

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
print(tree.in_balance(tree))
#assert tree.in_order_traversal(tree) == [1, 2, 3, 4, 5, 6, 7]
#assert tree.contains(tree, 3)
#assert not tree.contains(tree, 20)
#assert tree.max_depth(tree) <= 2

tree = Node()

tree.insert(2)
tree.insert(10)
tree.insert(3)
tree.insert(5)
tree.insert(100)

#assert tree.max_depth(tree) <= 2