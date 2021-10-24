"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    a = text.split()
    lst = []
    for i in a:
        if i == '!' or i == '?':
            lst.append(i)
        else:
            x = i[1:] + i[0] + 'ay'
            lst.append(x)
    result = ' '.join(lst)
    return result
  

