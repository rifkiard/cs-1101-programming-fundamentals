def write_file():
    file_name = input("Enter file name ...\n")
    data = input("Enter some data to store ...\n")

    try:
        fout = open(file_name + '.txt', 'w')
        fout.write(data)
        fout.close()

        print("Data stored successfully")
    except FileNotFoundError:
        print("The '/' character is not permitted, please try again.")
        write_file()


write_file()