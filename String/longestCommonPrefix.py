from typing import *
# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    if len(strs) == 0:
        return prefix
    sortedStrs = sorted(strs)
    firstWord, lastWord = sortedStrs[0], sortedStrs[-1]
    for i in range(0, len(firstWord)):
        if i < len(lastWord):
            if firstWord[i] == lastWord[i]:
                prefix += firstWord[i]
            else:
                return prefix
    return prefix
