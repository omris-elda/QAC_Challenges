# Given a string, return the number of times "am" appears in the string BUT ONLY WHEN "am" is not followed or preceded by any other LETTERS. 
# eg

# name("Am I in Amsterdam") → 1
# name("I am in Amsterdam am I?") → 2
# name("I have been in Amsterdam") → 0

 
# you should also attempt to write some tests for this function.

def amsterdam(input):
    try:
        input = str(input)
        input = input.lower()
        input = input.split()
        count = 0
        for word in input:
            if word == "am":
                count += 1
        return count
    except ValueError:
        return "Sorry, you've entered an incorrect value."
