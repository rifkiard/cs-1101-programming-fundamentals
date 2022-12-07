name = "rifki"
age = 19
gender = "male"

if name == "alex":
    print("Hi Alex. Where is Rifki?")
elif name == "hani":
    print("Hi Hani, where is Rifki?")
elif name == "rifki":
    if age == 19:
        if(gender == "male"):
            print("Hi Rifki, welcome back! I am glad you are here.")
        else:
            print("I am sorry, I don't know you yet.")
    else:
        print("I am sorry, I don't know you yet.")
else:
    print("I am sorry, I don't know you yet.")