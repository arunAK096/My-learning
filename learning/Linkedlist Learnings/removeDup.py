def remove_duplicates(self):
    if self.head is None:
        return

    node_values = set()

    current_node = self.head

    node_values.add(current_node.value)

    while current_node.next:

        if current_node.next.value in node_values:

            current_node.next = current_node.next.next
            self.length -= 1

        else:

            node_values.add(current_node.next.value)
            current_node = current_node.next

    self.tail = current_node