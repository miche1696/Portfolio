class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        toRet = [[1]]
        if numRows == 1:
            return toRet
        else:
            for i in range(2,numRows+1):
                row_prev = toRet[i-2]
                row_curr = [1]
                for n in range(len(row_prev)-1):
                    row_curr.append(row_prev[n] + row_prev[n+1])
                row_curr.append(1)
                toRet.append(row_curr)
            return toRet