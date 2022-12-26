#C reate a string that is a long series of words separated by spaces. 
#The string is your own creative choice. It can be names, favorite foods, animals, anything. 
#Just make it up yourself. Do not copy the string from another source. 

languages = "PHP Java JavaScript Python Ruby Perl Dart"
# print(languages)


# Turn the string into a list of words using split. 
languages = languages.split()
# print(languages)

# Delete three words from the list, but delete each one using a different kind of Python operation. 
# Sort the list. 
languages.pop(2)
del languages[5]
languages.remove("Ruby")

# print(languages)

# Sort the list. 
languages.sort()

# print(languages)

# Add new words to the list (three or more) using three different kinds of Python operations. 
languages.append("C#")
languageSwift = ["Swift"]
languages.extend(languageSwift)
languages += ["Kotlin"]

# print(languages)

# Turn the list of words back into a single string using join. 
languages = " ".join(languages)

# Print the string
print(languages)