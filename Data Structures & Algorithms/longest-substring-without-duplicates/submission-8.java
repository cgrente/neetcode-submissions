class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int best = 0;

        Set<Character> windowsState = new HashSet<>();
        for (int right = 0; right < s.length(); right++) {
            Character ch = s.charAt(right);
            while (windowsState.contains(ch)) {
                windowsState.remove(s.charAt(left));
                left = left +1;
            }
            windowsState.add(s.charAt(right));
            best = Math.max(best, right - left + 1);
        }

        return best;
    }
}
