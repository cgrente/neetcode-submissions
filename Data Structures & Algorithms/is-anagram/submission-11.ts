class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        // Your solution here
        if (s.length != t.length)
            return false

        const countCh = new Map<string, number>()

        for (const ch of s) {
            countCh.set(ch, (countCh.get(ch) ?? 0) + 1);
        }

        for (const ch of t) {
            const curr = countCh.get(ch)
            if (!curr)
                return false
            countCh.set(ch, curr - 1)
        }

        return true;
    }
}
