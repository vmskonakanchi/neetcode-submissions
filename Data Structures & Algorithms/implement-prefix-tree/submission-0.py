class Node:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.is_word = False

    def __str__(self):
        return (self.val + "*") if self.is_word else self.val

class PrefixTree:

    def __init__(self):
        self.root = Node("*")

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)

            cur = cur.children[c]

        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]

        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True