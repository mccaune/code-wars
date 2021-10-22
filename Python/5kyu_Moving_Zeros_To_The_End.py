"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(array):
    lst = []
    count = 0
    for i in array:
        if i != 0:
            lst.append(i)
        else:
            count += 1
    return lst + [0] * count
  

