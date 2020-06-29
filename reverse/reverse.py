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
        # set the current node to what is passed in
        current = node
        # if the head is none
        if self.head is None:
            # return
            return

        # if the next node from the head is none
        # list is only one node
        # print the only node value
        if self.head.next_node is None:
            print(current.value)

        # loop through the nodes
        # while the next is not none
        while current.next_node is not None:
            # if the next is none
            # we are at the tail
            if current.next_node is None:
                # print the value
                print(current.value)
                # delete the current node
                del current
            else:
                # otherwise recurse and run again on the next node
                next_node = current.get_next()
                self.reverse_list(next_node, current)
