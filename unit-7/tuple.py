student = {
    'FirstName': 'Emmanuel',
    'LastName':'Dahn',
    'Age': 35, 
    'Status': 'Freshman', 
    'Major': 'Computer science'
}

my_list = list(student.items())

print('student.items() = ',my_list)
print('Type of student.items() elements is ', type(my_list[1])) 
for x,y in student.items():  
    print(x,' is the key',  'and', y,' is the value')