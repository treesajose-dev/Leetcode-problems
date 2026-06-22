class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        max_vowel = 0
        max_consonant = 0

        for k, v in sorted(dict1.items(), key=lambda x: x[1], reverse=True):
            if k in vowels and max_vowel == 0:
                max_vowel = v

            if k not in vowels and max_consonant == 0:
                max_consonant = v

            if max_vowel and max_consonant:
                break

        return max_vowel + max_consonant