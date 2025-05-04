class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores the last seen index of each character
        start = 0        # start of current window
        max_length = 0   # result to return

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  # move the start past the last duplicate
            char_index[char] = i  # update last seen index
            max_length = max(max_length, i - start + 1)  # update max_length

        return max_length


