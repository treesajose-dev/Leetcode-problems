class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """

        steps=0 #initially steps is 0

        can=capacity #can filled with river water

        for i in range(len(plants)):
            if plants[i]<=can:
                can=can-plants[i]
                steps+=1
            else: #water in can not sufficient
                steps+=2*i+1
                can=capacity #refill
                can=can-plants[i] #then water

        return steps
        