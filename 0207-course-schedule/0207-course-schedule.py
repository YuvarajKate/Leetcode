class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Step 2: Create visited array
        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(course: int) -> bool:
            if visited[course] == 1:  # Cycle detected
                return False
            if visited[course] == 2:  # Already fully processed
                return True
            
            # Mark as visiting
            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # Mark as visited
            visited[course] = 2
            return True

        # Step 3: Check all courses
        for i in range(numCourses):
            if visited[i] == 0:  # Unvisited
                if not dfs(i):
                    return False
        
        return True