from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hash_map = defaultdict(list)

        for i, letter in enumerate(t):
            hash_map[letter].append(i)

        current_pos = -1

        for letter in s:
            if letter not in hash_map:
                return False

            found = False

            for pos in hash_map[letter]:
                if pos > current_pos:
                    current_pos = pos
                    found = True
                    break

            if not found:
                return False

        return True