class Solution:
    def isValidSudoku1(self, board: List[List[str]]) -> bool: #FIRST TRY
            
        for row in board:
            horizontalrow = []
            for box in row:
                if box in horizontalrow:
                    return False
                elif box != ".":
                    horizontalrow.append(box)
        
        for i in range(len(board)):
            verticalrow = []
            for row in board:
                if row[i] in verticalrow:
                    return False
                elif row[i] != ".":
                    verticalrow.append(row[i])
        
        for box_row in range(3):
            for box_col in range(3):
                block = []
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        val = board[i][j]
                        if val in block:
                            return False
                        elif val != ".":
                            block.append(val)
        return True

    
    def isValidSudoku2(self, board: List[List[str]]) -> bool: #SECOND TRY

        cols = collections.defaultdict(set) #add dictionaries
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in rows[r] or
                    val in cols[c] or
                    val in sqrs[(r//3, c//3)]):
                    return False
                cols[c].add(val)
                rows[r].add(val)
                sqrs[(r//3, c//3)].add(val)
        return True
    

        def isValidSudoku3(self, board: List[List[str]]) -> bool: #THIRD TRY

            mymap =[]
            for x in range(9):
                for y in range(9):
                    val=board[x][y]
                    if val != '.':
                        mymap += [(x, val), (val, y), (x// 3, y// 3,val)] #reverse the y to prevent duplicates
            return len(mymap)==len(set(mymap))
