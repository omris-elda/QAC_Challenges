def timestable(number):
    # for col in range(1, number + 1):
    #     for row in range(1, number + 1):
    #         print(row * col, end ="\t")  # <-- this code all works fine.
    #     print("\n")
    value = ""
    for col in range(1, number + 1):
        for row in range(1, number + 1):
            value = value + str(row * col) + "\t"
        value = value + "\n"
    return value


number = input("What number would you like to add by? Large numbers will cause the program to stop working. ")
try:
    number = int(number)
    print(timestable(number))
except ValueError:
    print("Sorry, you've failed to follow the most basic of instructions.")
    print("This program will now close. Goodbye.")

