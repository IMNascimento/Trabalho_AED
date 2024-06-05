class TSNode:
    def __init__(self, date, value, left=None, right=None):
        self.date = date
        self.value = value
        self.left = left
        self.right = right

    def insert(self, date, value):
        if date < self.date:
            if self.left is None:
                self.left = TSNode(date, value)
            else:
                self.left.insert(date, value)
        else:
            if self.right is None:
                self.right = TSNode(date, value)
            else:
                self.right.insert(date, value)

    def remove(self, date):
        if date < self.date:
            if self.left:
                self.left = self.left.remove(date)
        elif date > self.date:
            if self.right:
                self.right = self.right.remove(date)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_larger_node = self.right.find_min()
            self.date, self.value = min_larger_node.date, min_larger_node.value
            self.right = self.right.remove(self.date)
        return self
    
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find(self, date):
        if self.date == date:
            return self.value
        elif date < self.date and self.left is not None:
            return self.left.find(date)
        elif date > self.date and self.right is not None:
            return self.right.find(date)
        return None