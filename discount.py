def greeting(hour):
    if hour < 12:
        # The code below is only executed when the hour argument is less than 12
        return 'Good morning'
    elif hour < 18:
        # The code below is only executed when the hour argument is greater than 11 and less than 18 
        return 'Good afternoon'
    else:
        # The code below is only executed when the hour argument is greater than 17
        return 'Good evening'

print(greeting(7))
# output = Good morning
# (printed in our terminal)

print(greeting(12))
# output = Good afternoon
# (printed in our terminal)

print(greeting(21))
# output = Good evening
# (printed in our terminal)