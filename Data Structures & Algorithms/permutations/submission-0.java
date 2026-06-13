class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> permutations = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        boolean[] used = new boolean[nums.length];

        backTracking(used, nums, current, permutations);

        return permutations;
    }

    private void backTracking(boolean[] used, int[] nums, List<Integer> current, List<List<Integer>> permutations) {
        if (current.size() == nums.length) {
            permutations.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            current.add(nums[i]);
            this.backTracking(used, nums, current, permutations);
            used[i] = false;
            current.remove(current.size() - 1);
        }
    }
}
