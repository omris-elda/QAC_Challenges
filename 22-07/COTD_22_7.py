"""
Write a function that accepts a sequence of whitespace separated words as a string input, 
sorts each item alphanumerically and removes any duplicate items, then returns the result as a string.
Write a test for this function.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be: 
again and hello makes perfect practice world

Hint: make use of the set() collection type!
"""

def order(input):
    newlist = sorted(list(set(input.split())))
    output = ""
    output = " ".join(newlist)
    # for i in newlist:
    #     output += i
    #     output += sep
    # output.strip()
    return output