class MNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def insert(self, value):
        if not self.children:
            self.children.append(MNode(value))
        else:
            closest = min(self.children, key=lambda child: abs(child.value - value))
            closest.insert(value)

    def remove(self, value):
        for child in self.children:
            if child.value == value:
                self.children.remove(child)
                break
            child.remove(value)
        return self

    def find(self, value):
        if self.value == value:
            return True
        for child in self.children:
            if child.find(value):
                return True
        return False