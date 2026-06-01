class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        Map<Character, Integer> isAnagramMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            isAnagramMap.merge(s.charAt(i), 1, Integer::sum);
            isAnagramMap.merge(t.charAt(i), -1, Integer::sum);
        }

        return isAnagramMap.values().stream().allMatch(v -> v == 0);
    }
}
