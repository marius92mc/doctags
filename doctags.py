#!/usr/local/bin/python3
# doctags.py
###############################################################################
# This program allows the creation of personal database of documents
# that the user has in a folder. It allows the creation of tags, as well
# as browsing and filtering the documents.
###############################################################################

import os                       # for file & folder operations


def view_database():
    my_docs = os.listdir("docs")
    my_docs.sort()
    if len(my_docs) <= 20:
        print("You have " + str(len(my_docs)) + " documents in the folder.")
        print("They  are: ")
        for document in my_docs:
            print(document)
    else:
        print("You have " + str(len(my_docs)) + " documents in the folder.")
        print("I will print them in groups of 20 per page.")
        curr_no = 0
        # go through every document
        for document in my_docs:
            # increment the counter and print out our info
            curr_no += 1
            print(str(curr_no) + '. ' + str(document))
            # if we've reached number 20, 40, ...,
            # ask the user if he wants to stop
            if curr_no % 20 == 0:
                print()
                print("-----But wait, there's more!-----")
                print()
                go_on = input("Press 'n' for next page or 'q' to quit. ")
                if go_on == 'q':
                    return


def filter_starting_letter():
    my_docs = os.listdir("docs")
    my_docs.sort()
    starting_letter = input("What letter would you like to filter on? ")
    match = [''] * 100000
    counter = 0
    for document in my_docs:
        if str(document[0][0]) == str(starting_letter):
            match[counter] = document
            counter += 1
    if counter == 0:
        print("There are no matches for documents whose title")
        print("starts with " + str(starting_letter) + ".")
    elif (counter <= 20) and (counter > 0):
        print("I found " + str(counter) + " matches.")
        print("Here they are: ")
        print('-----' + str(starting_letter) + '-----')
        for matched_doc in match:
            if matched_doc != '':
                print(matched_doc)
    else:
        print("There are " + str(len(match)) + " documents matching.")
        print("I will print them in groups of 20 per page.")
        print('-----' + str(starting_letter) + '-----')
        curr_no = 0
        for matched_doc in match:
            curr_no += 1
            print(str(curr_no) + ". " + str(document))
            if curr_no % 20 == 0:
                print()
                print("-----But wait, there's more!-----")
                print()
                go_on = input("Press 'n' for next page or 'q' to quit. ")
                if go_on == 'q':
                    return


def main():
    print("The program allows you to view, edit or filter")
    print("your documents stored in a specific folder.")
    print("To access a function, please enter the specific option:")
    print("============OPTIONS=====================")
    print("1. View entire database")
    print("\t 1a. Filter by starting letter")
    print("2. Query by specific field (Author, Title, Tag)")
    print("3. Edit entry")
    print("4. Open with default reader")
    print("5. Quit")
    print("========================================")
    choice = input("Your option: ")
    choices = ["1", "1a", "2", "3", "4", "5"]

    # validate choice
    while choice not in choices:
        print("Please enter a valid choice")
        choice = input()
    # perform specific action
    if choice == "1":
        view_database()
    elif choice == "1a":
        filter_starting_letter()
    # elif choice == "2":
    #     query_by_field()
    # elif choice == "3":
    #     edit_entry()
    # elif choice == "4":
    #     open_entry()
    # elif choice == "5":
    #     quit_program()


if __name__ == "__main__":
    main()

