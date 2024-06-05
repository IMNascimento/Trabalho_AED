class BinaryTreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTreeNode(key, value)
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(key, value)
            else:
                self.right.insert(key, value)

    def remove(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.remove(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.remove(key)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_larger_node = self.right.find_min()
            self.key, self.value = min_larger_node.key, min_larger_node.value
            self.right = self.right.remove(self.key)
        return self

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find(self, key):
        if self.key == key:
            return self.value
        elif key < self.key and self.left is not None:
            return self.left.find(key)
        elif key > self.key and self.right is not None:
            return self.right.find(key)
        return None