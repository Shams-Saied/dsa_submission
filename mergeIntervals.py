class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        prevInterval=intervals[0]
        i=1

        while(i<len(intervals)):
            if prevInterval[1]>=intervals[i][0]:
                if intervals[i][1]>=prevInterval[1]:
                    prevInterval[1]=intervals[i][1]
                    intervals.pop(i)
                else:
                    intervals.pop(i)
            else:
                prevInterval=intervals[i]
                i+=1

        return intervals

    

            



sol=Solution()

intervals = [[1,4],[4,5],[0,65]]

#sol.merge(intervals)

intervals.sort()

print(intervals)
