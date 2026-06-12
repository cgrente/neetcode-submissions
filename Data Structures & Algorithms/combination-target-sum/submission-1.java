class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> uniqueCombination = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        int index = 0;

        backTracking(index, nums, target, current, uniqueCombination);

        return uniqueCombination;
    }

    private void backTracking(int index, int[] nums, int target, List<Integer> current, List<List<Integer>> uniqueCombination) {
        int currentSum = current.stream().mapToInt(Integer::intValue).sum();
        
        if (currentSum == target) {
            uniqueCombination.add(new ArrayList<>(current));
            return;
        }

        if (index >= nums.length || currentSum > target) {
            return;
        }

        current.add(nums[index]);
        this.backTracking(index, nums, target, current, uniqueCombination);
        current.remove(current.size() - 1);
        this.backTracking(index + 1, nums, target, current, uniqueCombination);
    }
}
