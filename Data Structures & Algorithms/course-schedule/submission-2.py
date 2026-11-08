class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            indegree[b] += 1
            graph[a].append(b)

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            indegree[course] -= 1
            for pre in graph[course]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        return finish == numCourses
