class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # On ne démarre le comptage que si c'est le DÉBUT d'une séquence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # On compte combien de nombres consécutifs suivent
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                if current_streak > longest_streak:
                    longest_streak = current_streak

        return longest_streak