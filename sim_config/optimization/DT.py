"""
Decision Tree.
"""

class DT:
    
    def __init__(self):
        """
        """


class Node:

    def __init__(self):
        """
        """
        
        self.left = None
        self.right = None
        
        self.left_weight = None
        self.right_weight = None


    @left.setter
    def left(self, node):
        self.left = node


    @right.setter
    def right(self, node):
        self.right = node


    @left_weight.setter
    def left_weight(self, weight):
        self.left_weight = weight


    @right_weight.setter
    def left_weight(self, weight):
        self.right_weight = weight