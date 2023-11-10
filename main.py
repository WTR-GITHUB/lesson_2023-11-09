import my_functions as mf
import os

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
Done_2 = ""
Enter_2 = ""
Done_3 = ""
Enter_3 = ""
Done_4 = ""
Enter_4 = ""
Done_5= ""
Enter_5 = ""
Done_6 = ""
Enter_6 = ""
Done_7 = ""
Enter_7 = ""
wrong_key = ""

while True:

    meniu_text = f"""
    Please chose what would you like to recieve:
    
    Enter '1' to get a list of letters ordered {Done_1}{Enter_1}
    Enter '2' to get a list of letters in reversed order {Done_2}{Enter_2}
    Enter '3' to get a list of unique letters {Done_3}{Enter_3}
    Enter '4' to get a list of numbers ordered {Done_4}{Enter_4}
    Enter '5' to get a list of numbers in reversed order {Done_5}{Enter_5}
    Enter '6' to get a list of unique nubers {Done_6}{Enter_6}
    Enter '7' to get a list of special simbols entered {Done_7}{Enter_7}
    Enter 'q' to exit program

    You have entered: {user_string}
    {wrong_key}
    """
    os.system('cls||clear')
    print(meniu_text)
    user_key = input()
    wrong_key = ""

    if user_key == "q":
        exit()
    elif user_key == "1":
        Enter_1 = str(mf.put_in_order(mf.sepacate_letters(user_string))) + "\n"
        Done_1 = "... Done \n"
    elif user_key == "2":
        Enter_2 = mf.put_in_order(mf.sepacate_letters(user_string))
        Enter_2 = str(mf.revers_order(Enter_2)) + "\n"
        Done_2 = "... Done \n"        
    elif user_key == "3":
        Enter_3 = mf.put_in_order(mf.sepacate_letters(user_string))
        Enter_3 = str(mf.sort_unique_chars(Enter_3)) + "\n"
        Done_3 = "... Done \n"
    elif user_key == "4":
        Enter_4 = str(mf.put_in_order(mf.sepacate_numbers(user_string))) + "\n"
        Done_4 = "... Done \n"
    elif user_key == "5":
        Enter_5 = mf.put_in_order(mf.sepacate_numbers(user_string))
        Enter_5 = str(mf.revers_order(Enter_5)) + "\n"
        Done_5 = "... Done \n"        
    elif user_key == "6":
        Enter_6 = mf.put_in_order(mf.sepacate_numbers(user_string))
        Enter_6 = str(mf.sort_unique_chars(Enter_6)) + "\n"
        Done_6 = "... Done \n"
    elif user_key == "7":
        Enter_7 = str((mf.sepacate_spec_simbols(user_string))) + "\n"
        Done_7 = "... Done \n"
    else:
        wrong_key = f"\n You have entered '{user_key}' a bad key, please do better."