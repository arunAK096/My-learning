def remove(self, index):
    if index < -1 or index >= self.length:
        return None 

    if index == 0:
        return self.pop_first()
    
    if index == self.length - 1 or index == -1:
        return self.pop()

    prev = self.get(index - 1)
    target = prev.next
    prev.next = target.next
    target.next = None
    self.length -= 1
    return target