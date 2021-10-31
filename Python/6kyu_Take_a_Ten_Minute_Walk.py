"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

#some test cases for you...
test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
test.expect(not is_valid_walk(['w']), 'should return False');
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');
"""

def is_valid_walk(walk):
    d = {}
    for i in walk:
        d[i] = d.get(i, 0) + 1

    y = d.get('n', 0) - d.get('s', 0)
    x = d.get('w', 0) - d.get('e', 0)
    count = sum(list(d.values()))

    if x == 0 and y == 0 and count == 10:
        return True
    else:
        return False
    

