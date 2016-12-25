

print("string exercises")


#count the number of characters (character frequency) in a string.
#easy way: go through the alphabet and just count each
#other way:  get letter 1 -> make sure its not in list -> count -> add to list -> 2nd letter, repeat

def letter_count(arg_string):
    string_matrix = []
    print(string_matrix[0])
    print("/n")
    string_matrix.append([])

    for i in range(0,len(arg_string)):
        if arg_string[i] not in string_matrix[i]:
            string_matrix.append([])
            string_matrix[i] = []
            string_matrix[i].append(arg_string[i])
            string_matrix[i].append(arg_string.count(arg_string[i]))
            #string_matrix.append(0)

    return string_matrix


print(letter_count("hello"))
