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

    def __str__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next

            if temp_node == self.head:
                break

            result += " -> "

        return result

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

    def split_list(self):
        if self.length == 0:
            return None, None

        mid = (self.length + 1) // 2
        count = 1

        first_list = CSLinkedList()
        second_list = CSLinkedList()

        current = self.head
        last_first_list = None

        while count <= mid:
            first_list.append(current.value)
            last_first_list = current
            current = current.next
            count += 1

        if last_first_list:
            first_list.tail = last_first_list
            first_list.tail.next = first_list.head

        while current != self.head:
            second_list.append(current.value)
            current = current.next

        if second_list.length > 0:
            second_list.tail = self.tail
            second_list.tail.next = second_list.head

        return first_list, second_list