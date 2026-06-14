class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> subsetWithoutDup = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        int index = 0;

        Arrays.sort(nums);

        this.backTracking(index, nums, current, subsetWithoutDup);

        return subsetWithoutDup;
    }

    private void backTracking(int index, int[] nums, List<Integer> current, List<List<Integer>> subsetWithoutDup) {
        if (index == nums.length) {
            subsetWithoutDup.add(new ArrayList<>(current));
            return;
        }

        current.add(nums[index]);
        this.backTracking(index + 1, nums, current, subsetWithoutDup);
        current.remove(current.size() - 1);

        int next = index + 1;
        while (next < nums.length && nums[next] == nums[index]) {
            next++;
        }

        this.backTracking(next, nums, current, subsetWithoutDup);
    }
}
