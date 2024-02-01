function combinationSum2(candidates: number[], target: number): number[][] {
    const res : number[][] = [];
    const path : number[] = [];
    let sum : number = 0;
    
    candidates.sort((a, b) => a - b);
    
    function backtrack(start: number) : void {
        if (sum === target) {
            res.push([...path]);
            return;
        }
        
        for (let i = start; i < candidates.length; i++) {
            if (i !== start && candidates[i] === candidates[i - 1]) {
                continue;
            }
            
            if (candidates[i] + sum > target) {
                return;
            }
            
            path.push(candidates[i]);
            sum += candidates[i];
            backtrack(i + 1);
            sum -= candidates[i];
            path.pop();
        }
    }

    backtrack(0);
    return res;
    
};