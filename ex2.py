def substrings_count_non_overlapping(s, sub):
    if sub not in s:
        return 0
    return s.count(sub)

print(substrings_count_non_overlapping("aaaa", "aa"))
print(substrings_count_non_overlapping("abcabc", "abc"))
print(substrings_count_non_overlapping("abc", "z"))
print(substrings_count_non_overlapping("a", "a"))
