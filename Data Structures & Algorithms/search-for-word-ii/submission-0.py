class Node:
    def __init__(self,val):
        self.val = val
        self.is_word = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_trie(words)
        cur = root 

        rows = len(board)
        cols = len(board[0])
        res = set()
        visited = set()

        def dfs(r, c , node, word, visited):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited:
                return

            char = board[r][c]
            if char not in node.children:
                return

            visited.add((r,c))
            node = node.children[char]
            word += char
            if node.is_word:
                res.add(word)

            dfs(r + 1, c, node, word,visited)
            dfs(r - 1, c, node, word,visited)
            dfs(r, c + 1, node, word,visited)
            dfs(r, c - 1, node, word,visited)
            visited.remove((r,c))

        
        for r in range(rows):
            for c in range(cols):
                cur = root
                dfs(r,c,cur, "",visited)

        return list(res)

    def build_trie(self,words:List[str]):
        root = Node("*")

        for word in words:
            cur = root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node(c)
                cur = cur.children[c]
            cur.is_word = True

        return root