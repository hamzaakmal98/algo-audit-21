class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            newr = [1]
            for j in range(len(row) - 1):
                newr.append(row[j] + row[j+1])
            newr.append(1)
            row = newr
        return row