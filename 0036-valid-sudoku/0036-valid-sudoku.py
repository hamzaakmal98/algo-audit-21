class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]

                if element != ".":
                    if element in rows[i]:
                        return False
                    rows[i].add(element)

                    if element in cols[j]:
                        return False
                    cols[j].add(element)

                    box_num = (i//3 * 3)+ j//3
                    if element in boxes[box_num]:
                        return False
                    boxes[box_num].add(element)

        return True

        




        