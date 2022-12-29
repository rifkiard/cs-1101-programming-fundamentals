# Python code examples to describe how tuples can be useful with loops over lists and dictionaries
# Should include: the zip function, the enumerate function, and the items method. 

# list zip
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
mos = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
events = ["New Year", "Valentine", "St. Patrick's Day", "Easter Egg", "Cinco De Mayo", "Super Pineapple Party","Summer Festival", "Friendship Day", "Harvest Festival", "Halloween", "Thanksgiving", "Winter Festival"]

x = 1
for tup in zip(months, mos, events):
    print(str(x) + ":")
    print(tup)
    print("The", tup[0], "(" + tup[1] + ")", "event is" , tup[2])
    x += 1

lists = [5, 4, 3, 2, 1, 0]
for tup in enumerate(lists):
    print(tup)


person = {
    "first name": "Rifki",
    "last name": "Ardiansyah",
    "age": 20,
    "gender": "Male",
    "country": "Indonesia",
    "status": "Student",
    "major": "Computer Science",
    "school": "University of the People"
}

for tup in person.items():
    print(tup)