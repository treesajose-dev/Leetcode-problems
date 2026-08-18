class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        #assign highest value to city with most no. of edges.
        res=0
        cost=1
        conn=[0]*n #connection list [0,0,0,0,0]

        #gives each city has how many roads
        #conn [2,3,4,2,1]
        for road in roads:
            conn[road[0]]+=1
            conn[road[1]]+=1

        conn.sort()
        #conn[1,2,2,3,4]

        # each con from conn multipy with 1 to n

        # res=1*1 + 2*2 + 2*3 + 3*4 + 4*5
        for con in conn:
            res+=con*cost
            cost+=1
        return res



        