class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        visited = [0] * numCourses

        def has_cycle(course):
            if visited[course] == 1: # visiting
                return True
            if visited[course] == 2: # visited
                return False
            visited[course] = 1
            for pre in graph[course]:
                if has_cycle(pre):
                    return True
            visited[course] = 2
            return False
            

        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True
        
