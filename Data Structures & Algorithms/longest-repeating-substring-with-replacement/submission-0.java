class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int best = 0;
        int maxCount = 0;

        int[] counter = new int[26];
        for (int right = 0; right < s.length(); right++) {
            counter[s.charAt(right) - 'A'] += 1;
            maxCount = Math.max(maxCount, counter[s.charAt(right) - 'A']);
            while ((right-left + 1) - maxCount > k) {
                counter[s.charAt(left) - 'A'] -= 1;
                left++;
            }

            best = Math.max(best, right - left + 1);
        } 

        return best;
    }
}
