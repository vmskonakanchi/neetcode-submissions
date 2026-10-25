class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        n = self.head
        
        while index > 0 and n:
            n = n.next
            index -= 1

        return n.val if n else -1


    def insertHead(self, val: int) -> None:
        n = Node(val)
        n.next = self.head
        self.head = n
        self.size += 1

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.size += 1
            self.head = Node(val)
            return

        n = self.head

        while n.next is not None:
            n = n.next

        n.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False

        if index == 0:
            if self.head:
                self.head = self.head.next
                self.size -= 1
                return True
            return False

        n = self.head
        prev = None

        while index > 0:
            prev = n
            n = n.next
            index -= 1

        if n:
            prev.next = n.next
        
        self.size -= 1
        return True


    def getValues(self) -> List[int]:
        n = self.head
        vals = []

        while n:
            vals.append(n.val)
            n = n.next

        return vals
