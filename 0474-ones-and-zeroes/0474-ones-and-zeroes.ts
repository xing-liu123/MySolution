function findMaxForm(strs: string[], m: number, n: number): number {
    let dp : number[][] = Array.from({length: m + 1}, () => Array(n + 1).fill(0));
    
    const countNumber = (str : string) : {'0': number, '1': number} => {
        const counts : {'0': number, '1': number} = {'0': 0, '1': 0};
        str.split('').forEach((char: string) => {
            counts[char]++;
        })
        
        return counts;
    }
    
    for(let i = 0; i < strs.length; i++) {
        let counts: {'0': number, '1': number} = countNumber(strs[i]); 
        for (let j = m; j >= counts['0']; j--) {
            for (let k = n; k >= counts['1']; k--) {
                dp[j][k] = Math.max(dp[j][k], dp[j - counts['0']][k - counts['1']] + 1);
            }
        }
    }
    
    return dp[m][n];
};