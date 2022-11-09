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

    def  print_tree(self,tree, level = 0, prefix = ""):
        if tree.data:
            print(" "*(4*level) + prefix + str(tree.data))
            if tree.left:
                self.print_tree(tree.left, level = level +1, prefix = "L:")
            if tree.right:
                self.print_tree(tree.right, level = level +1, prefix = "R:")


    def inOrderTraversal(self, tree):
        result = []
        if tree:
            result = self.inOrderTraversal(tree.left)
            result.append(tree.data)
            result.extend(self.inOrderTraversal(tree.right))
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
    

##root = Node()
##root.data = 3
##
##node_2 = Node(10)
##node_3 = Node(1)
##
##root.left = node_3
##root.right = node_2


bin_tree = Node()
bin_tree.insert(10)
bin_tree.insert(2)
bin_tree.insert(20)
bin_tree.insert(100)
bin_tree.insert(15)
bin_tree.insert(1)
bin_tree.insert(3)


bin_tree.print_tree(bin_tree)
print(bin_tree.inOrderTraversal(bin_tree))
print(bin_tree.max_depth(bin_tree))
print(bin_tree.contains(bin_tree,16))
print(bin_tree.contains(bin_tree,15))
                    
