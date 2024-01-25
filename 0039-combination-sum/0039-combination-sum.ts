function combinationSum(candidates: number[], target: number): number[][] {
    const path: number[] = [];
    const res: number[][] = [];
    let sum = 0;
    
    candidates.sort((a, b) => a - b);
    
    function backtrack(start: number) : void {
        if (sum === target) {
            res.push([...path]);
            return;
        }
        
        for (let i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target) {
                return;
            }
            
            path.push(candidates[i]);
            sum += candidates[i];
            backtrack(i);
            sum -= candidates[i];
            path.pop();
        }
    }

    backtrack(0);
    return res;
};