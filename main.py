import my_functions as mf

user_string = input("Please enter text string not less than 25 simbols: \n")

all_good = False

while all_good == False:
    if user_string == "q":
        exit()
    elif mf.test_input_lenght(user_string) == False:
        user_string = input("Your imput have less than 25 simbols, please try again or press 'q' for exit: \n")
    elif len(mf.sepacate_letters(user_string)) == 0:
        user_string = input("Your imput does not have any letter, please try again or press 'q' for exit: \n")
    elif len(mf.sepacate_numbers(user_string)) == 0:
        user_string = input("Your imput does not have any number, please try again or press 'q' for exit: \n")
    else:
        all_good = True
    
Done_1 = ""
Enter_1 = ""

while True:

    meniu_text = f"""
    Please chose what would you like to recieve:
    Enter '1' to get a list of letters ordered {Done_1}{Enter_1}
    Enter '2' to get a list of letters in reversed order
    Enter '3' to get a list of unique letters
    Enter '4' to get a list of numbers ordered
    Enter '5' to get a list of numbers in reversed order
    Enter '6' to get a list of unique nubers
    Enter '7' to get a list of special simbols entered
    Enter 'q' to exit program
    """

    print(meniu_text, "\n")

    user_key = input()

    if user_key == "q":
        exit()
    elif user_key == "1":
        Enter_1 = "\n", mf.put_in_order(mf.sepacate_letters(user_string))
        Done_1 = ".. Done "
        
