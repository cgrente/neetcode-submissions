class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> distinctNums = new HashSet<>();

        for (int num: nums) {
            if (!distinctNums.add(num)) {
                return true;
            }
            
        }

        return false;
    }
}