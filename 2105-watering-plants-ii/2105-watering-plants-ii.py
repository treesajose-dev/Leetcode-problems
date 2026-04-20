class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        i = 0
        j = len(plants) - 1

        canA = capacityA
        canB = capacityB

        refills = 0

        while i < j:
            # Alice waters plant i
            if canA < plants[i]: 
                refills += 1
                canA = capacityA
            canA -= plants[i] #waters the plant
            i += 1 #moves to the next plant

            # Bob waters plant j
            if canB < plants[j]:
                refills += 1
                canB = capacityB
            canB -= plants[j]

            
            j -= 1

        # If both meet at same plant
        if i == j:
            if max(canA, canB) < plants[i]:
                refills += 1

        return refills