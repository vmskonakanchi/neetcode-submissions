class Graph:
    
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False

        if dst not in self.graph[src]:
            return False

        self.graph[src].remove(dst)

        return True

    def hasPath(self, src: int, dst: int) -> bool:
        """
            22: (23)
            23: (24)
            hasPath (22,24)
        """
        
        stack = [src]
        visited = set()

        while stack:
            node = stack.pop()
            visited.add(node)
            if node == dst:
                return True
            for n in self.graph[node]:
                if n not in visited:
                    stack.append(n)

        return False
