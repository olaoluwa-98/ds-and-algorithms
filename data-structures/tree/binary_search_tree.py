class BinarySearchTree:
    def __init__(self, data) -> None:
        """
        Initialize the root of the binary search tree
        """
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def insert(self, data) -> None:
        """
        Insert a new node into the binary search tree
        """
        if data > self.data:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = BinarySearchTree(data)
        else:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BinarySearchTree(data)


    def in_order_traversal(self):
        """
        Traverse left child, parent and right child order
        """
        if self.left_child:
            self.left_child.in_order_traversal()
        print(self.data)
        if self.right_child:
            self.right_child.in_order_traversal()

    def pre_order_traversal(self):
        """
        Traverse parent, left child and right child order
        """
        print(self.data)
        if self.left_child:
            self.left_child.pre_order_traversal()
        if self.right_child:
            self.right_child.pre_order_traversal()

    def post_order_traversal(self):
        """
        Traverse left child, right child order and parent
        """
        if self.left_child:
            self.left_child.post_order_traversal()
        if self.right_child:
            self.right_child.post_order_traversal()
        print(self.data)

    def bfs_traversal(self):
        """
        Traverse the tree level by level using a queue
        """
        queue = []
        queue.append(self)
        while(len(queue) > 0):
            print(queue[0].data)
            node = queue.pop(0)
            
            if node.left is not None: 
                queue.append(node.left) 

            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 