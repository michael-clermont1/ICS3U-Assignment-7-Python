#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: June 2022
# This program finds an element in a list


def element_finder(list_of_elements, element):
    # this function checks if the element occurs

    if element in list_of_elements:
        element = True

    return element


def main():
    # this function gets the marks

    elements = []

    # input
    while True:
        try:
            element = int(input("Enter a number to enter into the array: "))
            elements.append(element)
            while element != -1:
                element = int(
                    input("Enter a number to enter into the array, -1 to stop: ")
                )
                elements.append(element)
            element_to_find = int(input("Enter a number check if it's in the array: "))
            elements.pop()
            break
        except Exception:
            print("That is not a number, try again.")
            continue
    found_element = element_finder(elements, element_to_find)
    if found_element == True:
        print("\nThe element was inside the list.")
    else:
        print("\nThe element was not inside the list.")

    print("\nDone.")


if __name__ == "__main__":
    main()
