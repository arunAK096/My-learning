class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

    def delete_by_value(self, value):

        if self.length == 0:
            return False

        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True

        prev = None
        current = self.head

        while True:

            if current.value == value:

                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head

                else:
                    prev.next = current.next

                    if current == self.tail:
                        self.tail = prev

                self.length -= 1
                return True

            prev = current
            current = current.next

            if current == self.head:
                break

        return False