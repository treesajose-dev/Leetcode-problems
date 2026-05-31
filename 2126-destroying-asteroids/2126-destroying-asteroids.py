class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """

        asteroids.sort()

        for x in asteroids:
            if mass < x:
                return False

            mass+=x

        return True
        