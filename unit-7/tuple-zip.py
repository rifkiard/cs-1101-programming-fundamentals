fruits = ['Apple','Banana','Grapes', 'Orange'] 
prices = ['$20.00','$15.00','$10.00', '$23.00'] 
zipped = tuple(zip(fruits, prices))  
print ('zipped = ',zipped)
print('Type of zipped elements is ',type(zipped[1]))

for fruits,prices in zipped:
    print(fruits,prices)