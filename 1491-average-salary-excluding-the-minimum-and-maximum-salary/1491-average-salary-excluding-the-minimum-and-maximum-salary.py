class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        new_sal=salary[1:]
        n_sal=new_sal[:-1]
        s=sum(n_sal)
        return float(s) / len(n_sal)

        