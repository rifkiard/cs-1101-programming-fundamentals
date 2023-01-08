def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]

        for li in val:
            if li not in inverse:
                inverse[li] = [key]
            else:
                inverse[li].append(key)

    return inverse

def string_to_list(string):
    raw_list = string.split(',')
    final_list = []
    for v in raw_list:
        final_list.append(v.strip())

    return final_list

original_file = open('original.txt', 'r')
write_inverted_file = open('inverted.txt', 'w')

original = eval(original_file.read())
inverted = invert_dict(original)

print("Welcome, your current dictionary is:\n")
print(original)

print("\nYour current inverted dictionary is:\n")
print(inverted)

is_want_to_add = input("\nDo you want to add something to it? [y/n]\n")

if is_want_to_add.lower() == 'y':
    new_key = input("\nPlease insert a key:\n")
    new_val = input("\nPlease insert the values that separated with comma:\n")

    print("\nAdding new value ...")

    original[new_key.strip()] = string_to_list(new_val)
    inverted = invert_dict(original)

    print(f"\n{new_key.strip()} successfully added into the dictionary.")
    print("\nYour current dictionary is:\n")
    print(original)
    print("\nYour current inverted dictionary is:\n")
    print(inverted)

original_file.close() 

write_original_file = open('original.txt', 'w')
write_original_file.write(str(original))
write_original_file.close()

write_inverted_file.write(str(inverted))
write_inverted_file.close()

print("\nGood bye.")