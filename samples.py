

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

def replace_first(str_arg):
    #replace every char in a string same as first char, with $
    return str_arg[0] + str_arg[1:].replace(str_arg[0],'$')

def first_switch(str_arg0,str_arg1):
    return str_arg1[:2] + str_arg0[2:] + ' ' + str_arg0[:2] + str_arg1[2:]

def replace_index(index_arg,str_arg):
    return str_arg[:index_arg] + str_arg[index_arg+1:]

print(replace_index(2,'helo'))
# print(string_2s("ab"))
#print(replace_first('restart'))
