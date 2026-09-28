class Node:
    def __init__(self, val: str):
        self.val = val
        self.children = []
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        if word[0] not in self.words:
            self.words[word[0]] = Node(word[0])

        temp = self.words[word[0]]

        for c in word[1:]:
            has_found = False

            for child in temp.children:
                if child.val == c:
                    temp = child
                    has_found = True
                    break

            if not has_found:
                n = Node(c)
                temp.children.append(n)
                temp = n

        temp.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, remaining):
            # We consumed the entire pattern
            if not remaining:
                return node.is_end

            c = remaining[0]

            # Wildcard: try every possible child
            if c == '.':
                for child in node.children:
                    if dfs(child, remaining[1:]):
                        return True

                return False

            # Normal character: follow only matching child
            for child in node.children:
                if child.val == c:
                    if dfs(child, remaining[1:]):
                        return True

                    return False

            return False

        # First character
        c = word[0]

        if c == '.':
            # Wildcard at root: try every possible starting character
            for node in self.words.values():
                if dfs(node, word[1:]):
                    return True

            return False

        if c not in self.words:
            return False

        return dfs(self.words[c], word[1:])