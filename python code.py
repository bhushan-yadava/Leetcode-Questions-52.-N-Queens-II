class Solution:
    def totalNQueens(self, n: int) -> int:
        

        # DFS function to try placing a queen on each row
        def dfs(row):
            # If all queens are placed successfully, increment the solution count
            if row == n:
                nonlocal solution_count
                solution_count += 1
                return
          
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Calculate indices for the diagonals
                pos_diag = row + col
                neg_diag = row - col + n
              
                # Check if the column or the diagonals have a queen already
                if cols[col] or diag[pos_diag] or anti_diag[neg_diag]:
                    continue  # Skip if there's a conflict
              
                # Place the queen and mark the places as attacked
                cols[col] = diag[pos_diag] = anti_diag[neg_diag] = True
                # Recursively place queen in the next row
                dfs(row + 1)
                # Backtrack and remove the queen from the current spot
                cols[col] = diag[pos_diag] = anti_diag[neg_diag] = False

        # Arrays to keep track of attacked columns and diagonals
        cols = [False] * n  # Columns where the queens can attack
        diag = [False] * (2 * n)  # Positive diagonals (index = row + col)
        anti_diag = [False] * (2 * n)  # Negative diagonals (index = row - col + n)
      
        solution_count = 0  # Counter for number of valid solutions
        # Start the DFS recursion from the first row
        dfs(0)
        # Return the total number of valid solutions found
        return solution_count
