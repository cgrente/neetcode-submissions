class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length ; i++) {
            int looking = target - nums[i];
            
            if (seen.containsKey(looking)) {
                int[] res = new int[2];

                res[0] = seen.get(looking);
                res[1] = i;

                return res; 
            }

            seen.put(nums[i], i);
        }

        return new int[0];
    }
}
