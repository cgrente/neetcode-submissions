class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting (in current path), 2 = done
        state = [0] * numCourses

        def has_cycle(course):
            if state[course] == 1:  # found a cycle
                return True
            if state[course] == 2:  # already verified, no cycle
                return False

            state[course] = 1  # mark as visiting

            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True

            state[course] = 2  # mark as done
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True