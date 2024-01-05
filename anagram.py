import string


class Solution(object):
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            print("Lengths of strings do not match. Cannot be anagram.")
            return False

        print("Lengths of strings match. Checking for anagram.")
        # Subtract the ordinal value of the alphabet from the ord value of "a".
        # Use the difference as the index of the char_map to set to 1 for str s
        # and -1 for str t.
        # If all the alphabets are the same, all the indices of the char_map
        # will be set to 0 [1 + (-1),].
        # Resulting in all values of the list being evaluated to 0. Returns True.
        char_map = [0] * 26
        for i in range(len(s)):
            char_map[ord(s[i]) - ord('a')] += 1
            char_map[ord(t[i]) - ord('a')] -= 1
            print(char_map)

        return all(count == 0 for count in char_map)


if __name__ == "__main__":
    SHOW = False
    S = "test"
    T = "tset"

    if SHOW:
        alphabets = list(string.ascii_lowercase)
        for i, alphabet in enumerate(alphabets):
            print(f"{alphabet} ordinal value {ord(alphabet)}")

    solu = Solution()
    ans = solu.isAnagram(S, T)
    print(ans)
