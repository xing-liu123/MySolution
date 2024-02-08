/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    const solve = () => {
        for (let i = 0; i < 9; i++) {
           
            for (let j = 0; j < 9; j++) {
                 if (board[i][j] !== '.') {
                    continue;
                }
                for (let k = 1; k <= 9; k++) {
                    if (isValid(i, j, k.toString())) {
                         board[i][j] = k.toString();
                        if (solve()) {
                            return true;
                        }
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
        return true;
    }
    
    const isValid = (row, col, val) => {
        for (let i = 0; i < 9; i++) {
            if (board[i][col] === val) {
                return false;
            }
        }
        
        for (let j = 0; j < 9; j++) {
            if (board[row][j] === val) {
                return false;
            }
        }
        
        
        for (let i = Math.floor(row / 3) * 3; i <  Math.floor(row / 3) * 3 + 3; i++) {
            for (let j = Math.floor(col / 3) * 3; j < Math.floor(col / 3) * 3 + 3; j++) {
                 if (board[i][j] === val) {
                    return false;
                }
            }
        }
        return true;
    }
    
    solve();
    return board;
};