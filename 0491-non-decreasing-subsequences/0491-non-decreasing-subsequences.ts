function findSubsequences(nums: number[]): number[][] {
    const res : number[][] = [];
    const subs : number[] = [];
    
    function backtrack(start : number) : void {
        if (subs.length > 1) {
            res.push([...subs]);
        }
        
        const mySet : Set<number> = new Set();
    
        for (let i = start; i < nums.length; i++) {
            if (mySet.has(nums[i])) {
                continue;
            }
            
            if (subs.length === 0 || nums[i] >= subs[subs.length - 1]) {
                mySet.add(nums[i]);
                subs.push(nums[i]);
                backtrack(i + 1);
                subs.pop();
            }
        }
        
    }
    
    backtrack(0);
    return res;
};