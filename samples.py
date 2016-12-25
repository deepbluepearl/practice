

print("string exercises")


#count the number of characters (character frequency) in a string.
#easy way: go through the alphabet and just count each
#other way:  get letter 1 -> make sure its not in list -> count -> add to list -> 2nd letter, repeat

def letter_count(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
    # not my answer, copied from w3

# print(letter_count('ted'))

# get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string
def string_2s(str_arg):
    if len(str_arg) > 1:
        return str_arg[0:2] + str_arg[-2:]
    return ""

print(string_2s("ab"))
