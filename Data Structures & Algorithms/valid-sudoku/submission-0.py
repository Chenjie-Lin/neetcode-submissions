class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":

                    if c not in rows[i]:
                        rows[i].add(c)
                    else:
                        return False

                    if c not in cols[j]:
                        cols[j].add(c)
                    else:
                        return False
                    
                    boxi = (i // 3) * 3 + (j // 3)

                    if c not in boxes[boxi]:
                        boxes[boxi].add(c)
                    else:
                        return False
        return True
        