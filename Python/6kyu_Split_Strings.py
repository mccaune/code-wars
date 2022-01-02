"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    i = 0
    result = []
    while i < len(s):
        try:
            a = s[i] + s[i+1]
            result.append(a)
            i += 2
        except:
            a = s[i] + '_'
            result.append(a)
            i += 1
    return result

