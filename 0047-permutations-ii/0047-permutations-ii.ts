function permuteUnique(nums: number[]): number[][] {
    const res : number[][] = [];
    const per : number[] = [];
    const used : boolean[] = new Array(nums.length).fill(false);
    
    nums.sort((a, b) => a - b);
    
    function backtrack() : void {
        if (per.length === nums.length) {
            res.push([...per]);
            return;
        }
        
        for (let i = 0; i < nums.length; i++) {
            if (used[i] || (i !== 0 && nums[i] === nums[i - 1] && !used[i - 1])) {
                continue;
            }
            
            used[i] = true;
            per.push(nums[i]);
            backtrack();
            per.pop();
            used[i] = false;
        }
    }

    backtrack();
    return res;
};