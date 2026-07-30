def is_sorted(self):

    if self.head is None or self.head.next == self.head:
        return True

    temp = self.head

    while temp.next != self.head:

        if temp.data > temp.next.data:
            return False

        temp = temp.next

    return True