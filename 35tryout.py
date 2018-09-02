def f():
    choice = input("Please input a value: \n> ")

    if choice == "1" or choice == "2": 
        # cannot simplify into choice == "1" or "2"
        print(f"The input is {choice}.")
    elif "3" in choice or "4" in choice:
        print(f"{choice} is not a good option.")
    elif choice == "5" or choice == "6":
        print("That's a good choice.")
    else:
        print('Hello World')

f()
# the function must be initiated at the end.

