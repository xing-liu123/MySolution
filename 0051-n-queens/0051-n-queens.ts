function solveNQueens(n: number): string[][] {
    const board : string[][] = Array(n).fill(null).map(() => Array(n).fill("."));
    
    let res : string[][] = [];
    
    const backtrack = (row : number): void => {
        if (row === n) {
            res.push(board.map(row => row.join("")));
            return;
        }
        
        for (let col = 0; col < n; col++) {
            if (isValid(row, col)) {
                board[row][col] = "Q";
                backtrack(row + 1);
                board[row][col] = ".";
            }
        }
    }
    
    const isValid = (row: number, col: number): boolean => {
        for (let i = row - 1; i >= 0; i--) {
            if (board[i][col] === "Q") {
                return false;
            }
        }
        
        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === "Q") {
                return false;
            }
        }
        
        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] === "Q") {
                return false;
            }
        }
        
        return true;
    }

    backtrack(0);
    return res;
};