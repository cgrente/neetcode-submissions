class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = defaultdict(list)
        for a, b in prerequisites:
            graphs[b].append(a)

        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting: 
                return False
            if node in visited: 
                return True

            visiting.add(node)

            for neighboor in graphs[node]:
                if dfs(neighboor) == False:
                    return False
                
            visiting.remove(node)
            visited.add(node)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False

        return True

        