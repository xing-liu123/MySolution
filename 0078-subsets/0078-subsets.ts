function subsets(nums: number[]): number[][] {
    const res : number[][] = [];
    const subset : number[] = [];
    
    function backtrack(start: number) : void {
        res.push([...subset]);
        
        for (let i = start; i < nums.length; i++) {
            subset.push(nums[i]);
            backtrack(i + 1);
            subset.pop();
        }
    }

    backtrack(0);
    return res;
};