# -*- encoding:utf-8 -*-
from __future__ import print_function

class BSTNode(object):

    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    # Returns a reference to a node of a specified key
    def get(self, key):
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    # Adds an element to a sub-tree
    def add(self, key):
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)

    # Removes an element of the specified key
    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            t = self.right._min()
            self.key, self.value = t.key, t.value
            self.right._deleteMin()
        return self

    # Retorns the minimum element of the sub-tree
    def _min(self):
        if self.left is None:
            return self
        else:
            return self.left._min()

    # Delete the minimum element of the sub-tree
    def _deleteMin(self):
        if self.left is None:
            return self.right
        self.left = self.left._deleteMin()
        return self

    # Traverse the tree in the order specified in the parameter (pre, pos, in or breadth)
    # visiting the nodes with the visit() function
    def traverse(self, visit, order='pre'):
        if order == 'breadth':
            l = []
            l.append(self)
            c = 0
            while c < len(l):
                v = l[c]
                for w in [v.left, v.right]:
                    if w is not None:
                        l.append(w)
                visit(v.key)
                c = c + 1
            return
        if order == 'pre':
            visit(self.key)
        if self.left is not None:
            self.left.traverse(visit, order)
        if order == 'in':
            visit(self.key)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'pos':
            visit(self.key)

    # Prints the tree
    def print(self, order='pre'):
        self.traverse(print, order)


if __name__ == '__main__':
    tree = BSTNode('F')
    tree.add('B')
    tree.add('G')
    tree.add('A')
    tree.add('D')
    tree.add('I')
    tree.add('C')
    tree.add('E')
    tree.add('H')
tree.print('breadth')
