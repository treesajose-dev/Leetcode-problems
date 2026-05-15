class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        neighbours=defaultdict(list)
        for n1,n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)

        q=deque([source]) # add 0 to deque
        seen=set([source])

        while q:
            node=q.popleft()
            if node==destination: #check if node is destination to end
                return True

            for n in neighbours[node]: # can visit only neighbours to reach destination
                if n not in seen:
                    seen.add(n)
                    q.append(n)
            
        return False
