# Nested lists
# list of the car brands

brands = [
    ["Hyundai", "Honda", "Lamborghini"],
    ["Toyota", "Suzuki", "Nissan"],
    ["BMW", "Bugatti", "Mazda"]
]
print(brands)
# Output of the code above:
# [['Hyundai', 'Honda', 'Lamborghini'], ['Toyota', 'Suzuki', 'Nissan'], ['BMW', 'Bugatti', 'Mazda']]

# The "*" operator:
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days3 = days * 3
print(days3)
# Output of the code above:
# ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# List slices:
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
part_months = months[3:6]
print(part_months)
# Output of the code above:
# ['April', 'May', 'June']


# The += operator
zodiacs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo"]
zodiacs += ["Virgo", "Libra", "Scorpio", "Sagittarius", "Capricon", "Aquarius", "Pisces"]
print(zodiacs)
# Output of the code above:
# ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricon', 'Aquarius', 'Pisces']


# A list filter 
names = ["Ana", "Azian", "Rasel", "Pian", "Asep"]

a_names = [n for n in names if n[0] == "A"]
print(a_names)
# The code above is filtering the names that start with letter A
# Output of the code above:
# ['Ana', 'Azian', 'Asep']

#A list operation that is legal but does the "wrong" thing, and not what the programmer expec
fruits = ["Banana", "Mango", "Watermelon", "Apple"]
fruits = fruits.append("Orange")

print(fruits)
# The code above will replacing the fruilts list with None value.
# Output of the code above:
# None