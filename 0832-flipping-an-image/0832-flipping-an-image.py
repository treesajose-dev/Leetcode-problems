class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        lis=[]
        for x in image:
            lis.append(x[::-1])
        
        for item in lis:
            for i in range(len(item)):
                if item[i]==0:
                    item[i]=1
                else:
                    item[i]=0
        return lis

        