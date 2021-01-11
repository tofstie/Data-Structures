"""The kinds included are:
        
        Node (forward linking)
        doubleNode (forward and backward linking)
        treeNode (Left Child, Right Child, and Parent)
        """
class Node:
    """This Node is a single forward linking node"""
    def __init__(self, value=None):
        """Intialize the Node class

            Keywords:
            Value -- the value that you want to set to the node. Default is None
            link -- the node that this node points to. When intializing, this is set to None 
            See Node.changeLink to set the link

        """
        self._value = value
        self._link = None
    
    def value(self):
        """Returns the value of the Node"""
        return self._value
    
    def link(self):
        """Returns the next Node"""
        return self._link

    def changeValue(self, newValue):
        """Changes the value stored in the node"""
        self._value = newValue

    def changeLink(self, newLink):
        """Changes the link in the node"""
        self._link = newLink


class treeNode:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._leftChild = None
        self._rightChild = None 

    def value(self):
        return self._value
    
    def getParent(self):
        return self._parent

    def leftChild(self):
        return self._leftChild

    def rightChild(self):
        return self._rightChild

    def setChild(self, newTreeNode):
        if newTreeNode.value() >= self.value():
            if self.leftChild() is None:
                self._leftChild = newTreeNode
                return
            else:
                self._leftChild.setChild(newTreeNode)
                return
        elif newTreeNode.value() < self.value():
            if self.rightChild() is None:
                self._rightChild = newTreeNode
                return
            else:
                self._rightChild.setChild(newTreeNode)
                return
            


