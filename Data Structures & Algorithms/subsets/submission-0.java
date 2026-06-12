class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> allPossibleSubsets = new ArrayList<>();
        List<Integer> current = new ArrayList();
        int index = 0;

        this.backTracking(index, nums, current, allPossibleSubsets);
        
        return allPossibleSubsets;
    }

    private void backTracking(int index, int[] nums, List<Integer> current, List<List<Integer>> allPossibleSubsets) {
        if (index == nums.length) {
            allPossibleSubsets.add(new ArrayList<>(current));
            return;
        }

        current.add(nums[index]);
        backTracking(index + 1, nums, current, allPossibleSubsets);
        current.remove(current.size() - 1);
        backTracking(index + 1, nums, current, allPossibleSubsets);

    }
}
