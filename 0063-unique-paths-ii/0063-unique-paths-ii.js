/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    let m = obstacleGrid.length;
    let n = obstacleGrid[0].length;
    
    const paths = new Array(m).fill(null).map(() => new Array(n).fill(0));
    
    for (let i = 0; i < m; i++) {
        if (obstacleGrid[i][0] === 1) {
            break;
        }
        paths[i][0] = 1;
    }
    
    for (let j = 0; j < n; j++) {
        if (obstacleGrid[0][j] === 1) {
            break;
        }
        paths[0][j] = 1;
    }
    
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (obstacleGrid[i][j] !== 1) {
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]; 
            }
        }
    }
    
    return paths[m - 1][n - 1];
};