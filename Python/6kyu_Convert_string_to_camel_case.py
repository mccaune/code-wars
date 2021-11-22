"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    lst = []
    i = 0
    while i < len(text):
        if text[i] == '_' or text[i] == '-':
            lst.append(text[i+1].upper())
            i += 2
        else:
            lst.append(text[i])
            i += 1
    return ''.join(lst)

