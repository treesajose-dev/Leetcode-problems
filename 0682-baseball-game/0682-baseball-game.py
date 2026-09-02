class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record=[]

        for x in operations:
            if x=="C":
                record.pop()
            elif x=="D":
                val=record.pop()
                record.extend([val,val*2])
            elif x=='+' and len(record)>=2:
                val1=record.pop()
                val2=record.pop()
                record.extend([val2,val1,val1+val2])
            else:
                record.append(int(x))

        return sum(record)




        