class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

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

    def right_rotation():
        
    def left_rotation():
        

    def in_balance(self, tree):
        left_depth = self.max_depth(self.left)
        right_depth = self.max_depth(self.right)
        
        if (right_depth - left_depth)**2 <= 1:
            return True
        else:
            return False
        
        return True if in_balance(self.left) and in_balance(self.right) else False

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