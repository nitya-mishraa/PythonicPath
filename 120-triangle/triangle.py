class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        row = len(triangle)
        dp = [[0] * len(triangle[i]) for i in range(row)]
        dp[0][0]= triangle[0][0]
        for i in range(1,row):
            #LEFT EDGE CASE
            dp [i][0] = triangle[i][0]+dp[i-1][0]

            #MIDDLE EDGE CASE
            for j in range(1, len(triangle[i])-1):
                dp[i][j]= triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])

            #RIGHT EDGE CASE
            dp[i][-1]=triangle[i][-1]+dp[i-1][-1]
        #RETURN MINIMUM PATH FROM LAST ROW OF DP
        return min(dp[-1])