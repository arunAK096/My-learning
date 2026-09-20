from Nodeclass import LinkedList


def remove_duplicates(ll: LinkedList):
        if ll.head is None:
            return
        current_node = ll.head
        prev_node = None
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
        ll.tail = prev_node
        return ll.head
        
        