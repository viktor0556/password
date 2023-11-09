users = {}             # This stores the usernames and passwords you entered
Attempts = 3           # To keep track of the number of login attempts allowed
pin_code = 9031        # We'll ask for this later with an input

# 'if' means that if the condition is true, the 'if' block will execute first. If it's not true, then 'elif' is checked.

# 'while' is a loop (the loop continues as long as the condition is true)
while True:

    # 'input' means the user can type into it, while 'print' just displays text and doesn't allow input afterward
    account = input("Do you already have an account? (yes/no): ") # Asks if you already have an account
    account = account.lower()  # Converts the input to lowercase automatically

    if account == "no":  # If the user chose "no"
        username = input("Choose a username: ")  # Then it asks for a username
        password = input("Choose a password: ")  # And a password
        users[username] = password  # Here, it stores them

    elif account == "yes":  # If you chose "yes" because you already have an account, this part is executed
        entered_username = input("Enter your username: ")  # Here, you can enter the username only if one already exists
        entered_password = input("Enter your password: ")  # Same for the password
        if account == "yes" and entered_username in users and users[entered_username] == entered_password: # If the username and password match
            print("Successful login")  # It prints "Successful login"
            break  # Here, it ends the loop, which means the code stops

        else:  # 'else' means that if 'if' and 'elif' didn't match
            print(f"Wrong password or username, try again. You have {Attempts} attempts left.")  # It displays that they didn't match and shows the remaining attempts
            Attempts -= 1  # The variable 'Attempts' was set to 3 at the top, and this decreases it by 1 for every wrong username or password

            if Attempts < 0:  # If the code reaches 0 attempts
                print("SYSTEM LOCKED")  # It prints "SYSTEM LOCKED"
                entered_pin_code = int(input("Enter the PIN code or you will be locked out!: "))  # 'int' means it only accepts whole numbers, and here you need to enter the PIN code
                if entered_pin_code == pin_code:  # If the entered PIN code matches the one set at the top
                    print("Successful Entry!")  # It prints "Successful Entry"
                else:  # If you didn't enter the PIN code correctly
                    print("Locked out!")  # It prints "Locked out"
                break  # It ends the 'while' loop, which stops the program

