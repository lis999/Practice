"""
Given a sequense of items and a specific item in that sequence, return the item immediately following the item
specified. If the item occurs more than once in a sequence, return the item after the first occurence.
This should work for a sequence of any type
next_item([1, 2, 3, 4, 5], 3) -> 4
"""

def next_item(xs, item):
    it = iter(xs)                        # iter - will make element iterable
    for x in it:
        if x == item:
            break
    return next(it, None)                # next - will return next element

print(next_item([1,2,3,4,5], 3))