d = {
    'FirstName': 'Emmanuel',
    'LastName':'Dahn',
    'Age': 35, 
    'Status': 'Freshman', 
    'Major': 'Computer science'
}

result = dict()
for key in d:
    val = d[key]
    if val not in result:
        result[val] = [key]
    else:
        result[val].append(key)


print(result)