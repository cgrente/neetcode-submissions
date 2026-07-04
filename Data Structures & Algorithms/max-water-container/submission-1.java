class Solution {
    public int maxArea(int[] heights) {
        int left = 0; 
        int right = heights.length - 1;

        int width = 0;
        int height = 0;
        int waterAmount = 0;
        while (left < right) {
            width = right - left;
            height = Math.min(heights[left], heights[right]);
            waterAmount = Math.max(waterAmount, width * height);

            if (heights[left] < heights[right])
                left++;
            else
                right--;
        }

        return waterAmount;
    }
}
