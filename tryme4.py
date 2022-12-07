# Name: Rifki Ardiansyah
# Course: CS 1101-01 - AY2023-T2
# Instructor: Laura Smith
# Date: Nov, 23 2022

# defining the "new_line" function. 
# It will print a dot in our terminal.
def new_line():
    print('.')

# defining the "three_line" function. 
# It will print three dots in our terminal.
def three_lines():
    new_line()
    new_line()
    new_line()

# defining the "nine_line" function. 
# It will print nine dots in our terminal, the dots is come from the three_lines function.
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# defining the "clear_screen" function. 
# It will print twenty-five dots in our terminal, the dots is come from the combination of nine_line, three_line, and new_line functions.
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# calling the nine_lines function.
nine_lines()
# output:
# .
# .
# .
# .
# .
# .
# .
# .
# .

# calling the clear_screen function.
clear_screen()
# output:
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .