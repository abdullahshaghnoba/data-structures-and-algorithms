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
              
         



if __name__=="__main__":
    node1 = Node("2")
    node1.left=Node("1")
    node1.left.left=Node("0")
    node1.right=Node("3")
    node1.right.right = Node("4")
    tree= Binary_Tree()
    # node12 = Node("A")
    # node12.left = Node("BBB")
    # node12.right = Node("CCCC")
    # node12.left.left = Node("D")
    # node12.left.right = Node("E")
    # node12.right.left = Node("k")
    # node12.right.right = Node("g")
    # tree2= Binary_Tree()

    print(tree.post_order(node1))
    # print(tree2.post_order(node12))

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
                    print(node.right.value)   
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
