class NumArray {
    private int[] nums;
    private int[] prefixSums;

    public NumArray(int[] nums) {
        this.nums = nums;
        this.initializePrefixNums();  
    }

    private void initializePrefixNums() {
        this.prefixSums = new int[this.nums.length + 1]; // default init at 0
        for (int i = 0; i < this.nums.length; i++) {
            this.prefixSums[i + 1] = this.prefixSums[i] + this.nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        return this.prefixSums[right + 1] - this.prefixSums[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */