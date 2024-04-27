class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        """Remove the last node from the list."""
        if self.tail is None:
            return None
        removed_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_node.data

    def shift(self):
        """Remove the first node from the list."""
        if self.head is None:
            return None
        removed_node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_node.data

    def unshift(self, data):
        """Add a new node to the beginning of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


dd_list = DoublyLinkedList()
dd_list.push(2)
dd_list.push(3)
dd_list.unshift(1)
dd_list.unshift(0)
value = dd_list.shift()
while value is not None:
    print(value)
    value = dd_list.shift()
