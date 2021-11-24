"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

import re

def is_pangram(s):
    x = re.findall("[a-z]", s.lower())
    d = {}
    for i in x:
        d[i] = d.get(i, 0) + 1
    return True if len(d) == 26 else False
    

