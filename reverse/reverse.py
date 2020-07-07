class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # # if the head is none
        if node is None:
            # return
            return

        # if the node after is none
        # node is the tail
        if node.next_node is None:
            # set the head to the tail node
            # which is now the 'node'
            self.head = node
            # set the next node to the 'prev' passed in value
            node.next_node = prev
            # return the node
            return node
        else:
            # set the next node in line
            next = node.next_node
            # set the nodes next_node
            # to the prev passed in node
            node.next_node = prev
            # recurse through the list
            self.reverse_list(next, node)
