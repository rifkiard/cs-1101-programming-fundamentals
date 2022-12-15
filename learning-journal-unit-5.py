# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     if(letter == "O" or letter == "Q"):
#         print(letter + "u" + suffix)
#     else:
#         print(letter + suffix)

def spell_it(string):
    x = 0
    while(x < len(string)):
        print(string[x:x+1])
        x += 1

spell_it("sunday")

def change_hero_gender(hero_name):
    return hero_name[0:len(hero_name) - 3] + "woman"

print(change_hero_gender("superman"))
print(change_hero_gender("spiderman"))
print(change_hero_gender("ironman"))
print(change_hero_gender("batman"))

def vowels_to_i(string):
    output = ""

    x = 0
    while(x < len(string)):
        current_letter = string[x:x+1]
        if(current_letter == "a" or current_letter == "e" or current_letter == "i" or current_letter == "o" or current_letter == "u"):
            output += "i"
        else:
            output += current_letter
        x += 1

    return output

print(vowels_to_i("Hello, are you all right?"))
print(vowels_to_i("My name is Rifki Ardiansyah"))


        