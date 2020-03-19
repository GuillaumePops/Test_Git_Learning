# def main():
#     # Variable list
#     user_name = 'Pops'
#     age = 31
#     # show the sentence
#     print('Hi' + user_name + ", You have " + str(age) + " years old!")
#     print(15 % 18)
#     print(1 / 2)


# def main():
#     # Collect the notes
#     note1 = input("Enter the first note: ")
#     note2 = input("Enter the second note: ")
#     note3 = input("Enter the third note: ")
#
#     # average note result
#     average_note = (int(note1) + int(note2) + int(note3)) / 3
#
#     # Show the average note
#     print("the note average is : ", str(average_note))

# def main():
#     # money in the wallet
#     wallet_money = int(input("how much do you have in your wallet: "))
#
#     # article
#     table = 50
#     # wallet money after purchase
#     wallet_money = wallet_money - table
#
#     # Show how much do you have after purchase
#     print("you have : ", str(wallet_money), "€ in your wallet after purchase")

# def main():
#     wallet = 5000
#     computer_price = 6000
#     if computer_price <= wallet and computer_price > 1000:
#     # if wallet >= computer_price > 1000:
#         print("you can buy the computer")
#         # wallet -= computer_price
#     else:
#         print("it is impossible to buy the computer, you only have {}€".format(wallet))
#
#     # Ternary condition
#     text = ("You can't buy it", "You can buy it")[computer_price <= wallet]
#     print(text)

# def main():
#     password = input('Enter your password ')
#     password_length = len(password)
#
#     if password_length <= 8:
#         print('Your password is too short')
#     elif 8 < password_length < 12:
#         print("password is okay")
#     else:
#         print("password is valid")

def main():
    age = int(input("How old are you?\n"))
    student = input("Are you student Y/N?\n")
    pop_corn_answer = input("Would you want some pop corn Y/N?\n")

    if pop_corn_answer == "Y" or pop_corn_answer == "y":
        pop_corn_size = input("What size do you want? Little, Medium, Large\n")
    else:
        pop_corn_size = "None"

    if pop_corn_size == "Little":
        pop_corn_prize = 3
    elif pop_corn_size == "Medium":
        pop_corn_prize = 6
    elif pop_corn_size == "Large":
        pop_corn_prize = 9
    else:
        pop_corn_prize = 0

    if age < 18:
        ticket_prize = 7
    elif student == "Y" or student == "y":
        ticket_prize = 10
    else:
        ticket_prize = 12

    total = ticket_prize + pop_corn_prize

    print("The total prize is {}".format(total))



if __name__ == '__main__':
    main()
