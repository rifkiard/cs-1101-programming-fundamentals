# def less_common_multiple(first_number, second_number):  
#     if first_number > second_number:  
#         greater = first_number  
#     else:  
#         greater = second_number  
#     while(True):  
#         if((greater % first_number == 0) and (greater % second_number == 0)):  
#             result = greater  
#             break  
#         greater += 1  
#     return result 

# example 1
def less_common_multiple(first_number, second_number):
    print(type(first_number))
    print(type(second_number))

    if(isinstance(first_number, int) != True):
        print("The first given argument (" + str(first_number) + ") is not an integer.")
        return
    elif(isinstance(second_number, int) != True):
        print("The second given argument (" + str(second_number) + ") is not an integer.")
        return

    if first_number > second_number:
        biggest_number = first_number
    else:
        biggest_number = second_number
    while(True):
    if((biggest_number % first_number == 0) and (biggest_number % second_number == 0)):
        result = biggest_number
        break
    biggest_number += 1
    print(result)
    return result

lcm = less_common_multiple(20,12)