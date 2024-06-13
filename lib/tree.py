
class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        stack = [self.root]

        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node['id'] == id:
                return node
            stack.extend(reversed(node['children']))
        return None