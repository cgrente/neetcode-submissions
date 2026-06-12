class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> uniqueCombination = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        int index = 0;

        backTracking(index, nums, target, current, uniqueCombination);

        return uniqueCombination;
    }

    private void backTracking(int index, int[] nums, int remaining, List<Integer> current, List<List<Integer>> uniqueCombination) {        
        if (remaining == 0) {
            uniqueCombination.add(new ArrayList<>(current));
            return;
        }

        if (remaining < 0 || index >= nums.length) {
            return;
        }

        current.add(nums[index]);
        this.backTracking(index, nums, remaining - nums[index], current, uniqueCombination);
        current.remove(current.size() - 1);
        this.backTracking(index + 1, nums, remaining, current, uniqueCombination);
    }
}
