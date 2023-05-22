class Node:
    """
    creats a node with atributes of value,left and right
    takes a value
    returns nothing
    """
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

#######################################################
class Binary_Tree:
    def __init__(self):
            self.root = None
            self.max = None
    """
    Sorts the tree on this order (the node then it's left node then it's right node) and keeps the sorted nodes in a list.
    Arguments: the root node in the tree.
    return: a list that contains the sorted nodes of the tree.
    """
    def pre_order(self,root=None,returned_list = None):
        if returned_list == None:
             returned_list=[]
        if root is not None:
            returned_list.append(root.value)
            self.pre_order(root.left,returned_list)
            self.pre_order(root.right,returned_list)
        return returned_list
    """
    Sorts the tree on this order (the left node then the node then the right node) and keeps the sorted nodes in a list.
    Arguments: the root node in the tree.
    return: a list that contains the sorted nodes of the tree.
    """
    def in_order(self,root=None,returned_list=None):
        if returned_list == None:
             returned_list=[]
        if root is not None:
              self.in_order(root.left,returned_list)
              returned_list.append(root.value)
              self.in_order(root.right,returned_list)
        return returned_list
    """
    Sorts the tree on this order (the left node then the right node then the node) and keeps the sorted nodes in a list.
    Arguments: the root node in the tree.
    return: a list that contains the sorted nodes of the tree.
    """
    def post_order(self,root=None,returned_list=None):
        if returned_list == None:
             returned_list=[]
        if root is not None:
              self.post_order(root.left,returned_list)
              self.post_order(root.right,returned_list)
              returned_list.append(root.value)
        return returned_list
    # def post_order(self,root):
    #     if root == None:
    #          return []
    #     if root is not None:
    #       return  self.post_order(root.left)+self.post_order(root.right)+[root.value]

    """
    finds the maximum value in a tree 
    Arguments: none
    Returns:the result of max_recursion() helper function
    """
    def find_maximum_value(self):
        if self.root == None:
            return "no max value for empty trees" 
         
        else:
            # print(self.root.value)
            return self.max_recursion(self.root)
        
                
    """
    helper function for the find_maximum_value method
    Arguments: root
    Returns: self.max
    """   
    def max_recursion(self,root):
        if root is not None:    
            if self.max == None:
                self.max=root.value
            if root.value > self.max:
                self.max=root.value
                # print(max)           
            self.max_recursion(root.left)
            self.max_recursion(root.right)
        return self.max


if __name__=="__main__":
    tree= Binary_Tree()
    node1 = Node(-5)
    tree.root = node1
    tree.root.left=Node(-7)
    tree.root.left.left=Node(-10)
    tree.root.left.right=Node(-6)
    tree.root.right=Node(-3)
    tree.root.right.right = Node(-2)
    tree.root.right.left = Node(-4)
    print(tree.find_maximum_value())
    tree2= Binary_Tree()
    node12 = Node(5)
    tree2.root = node12
    node12.left = Node(3)
    node12.right = Node(7)
    node12.left.left = Node(2)
    node12.left.right = Node(4)
    node12.right.left = Node(6)
    node12.right.right = Node(8)

    print(tree.in_order(node1))
    print(tree2.in_order(node12))

# ###############################################################
class Binary_Search_Tree(Binary_Tree):
    def __init__(self):
        super().__init__()
    """
    Adds a node in a tree in the correct position to make a binary search tree.
    Arguments: value --> the value of the node to be added
    returns nothing
    """
    def Add(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
             self.recursion(self.root,value)
    """
    helper function for the Add method to do the recursion process(search for the correct position for the node)
    Arguments: node --> the root node in the tree , value --> the value of the node to be added.
    returns nothing.
    """         
    def recursion(self,node,value):
            # print(node.value)
            if value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    # print(node.right.value)   
                else:
                    self.recursion(node.right,value)   
            else:
                if node.left is None:
                    node.left = Node(value)   
                else:
                    self.recursion(node.left,value)

    """
    searches if the tree contains a certain node.
    Arguments: value --> the value of the node we are searching for
    returns a boolean (True if the node is in the tree and False if not)
    """   
    def Contains(self, value):
        return self.recursive_search(self.root, value)
    """
    helper function for the Contains method to do the recursion process(search for the node)
    Arguments: node --> the root node in the tree , value --> the value of the node to be searched for.
    returns boolean(True if the node is in the tree and False if not).
    """ 
    def recursive_search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self.recursive_search(node.left, value)
        else:
            return self.recursive_search(node.right, value)   

if __name__=="__main__":       
    tree2 = Binary_Search_Tree()
    tree2.Add(2)
    tree2.Add(2)
    tree2.Add(1)
    tree2.Add(3)
    print(tree2.pre_order(tree2.root))
    print(tree2.Contains(5))
