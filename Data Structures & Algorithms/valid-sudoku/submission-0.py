class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        BREAK_CHAR = "."
        col_visited_numbers =[[] for _ in range(len(board))]
        box_visited_numbers = [set() for _ in range(len(board))]
        for row_index in range(0, len(board)):
            row = board[row_index]
            row_visited_numbers = []
            for cell_index in range(0, len(row)):
                cell = row[cell_index]
                if cell in col_visited_numbers[cell_index] and cell != BREAK_CHAR:
                    return False

                if cell in row_visited_numbers and cell != BREAK_CHAR:
                    return False

                # Get the current box
                box_row = row_index //3 
                box_col = cell_index // 3
                box_index = box_row * 3 + box_col

                if cell in box_visited_numbers[box_index] and cell != BREAK_CHAR:
                    return False

                box_visited_numbers[box_index].add(cell)
                row_visited_numbers.append(cell)
                col_visited_numbers[cell_index].append(cell)




        return True
