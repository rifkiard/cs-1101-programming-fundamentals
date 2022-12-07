def loading(n):
    if n <= 100:
        print(str(n) + '%')
        loading(n + 20)


def welcome():
    genderToHonorific = {
        "male": "Mr",
        "female": "Ms"
    }
    
    name = input("What is your name?\n")
    gender = input("what is your gender?\n")

    print("Loading ...")

    loading(0)

    if str(gender).lower() in genderToHonorific:
        print("Welcome back " + genderToHonorific[str(gender).lower()] + ". " + name)
    else:
        print("I am sorry, the gender that you input is not having an honorific available in the program yet, please re-run the program with another gender value.")

welcome()