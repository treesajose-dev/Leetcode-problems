class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj=[ [] for _ in range(numCourses) ]
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        vis=[False]*numCourses
        path=[False]*numCourses

        def dfs(node):
            vis[node]=path[node]=True
            for next_node in adj[node]:
                if not vis[next_node]:
                    if dfs(next_node):
                        return True
                elif path[next_node]:
                    return True
            path[node]=False
            return False

        for i in range (numCourses):
            if not vis[i]:
                if dfs(i): 
                    return False

        return True

        

            