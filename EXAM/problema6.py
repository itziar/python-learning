'''
Problem 6

Write a function to flatten a list. The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
'''

def flatten(lst):
    return sum( ([x] if not isinstance(x, list) else flatten(x)    for x in lst), [] )