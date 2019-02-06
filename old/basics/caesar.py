#!/usr/bin/python3.5
import sys

def main():
    # if len(sys.argv) < 2:
    #     print("Please enter possitive integer after name of your programme")
    #     exit(1)
    try:
        key = int(input("Please enter possitive integer after name of your programme: "))
    except ValueError:
        print("Invalid! Please enter number!")
        main()
    text = input("plaintext: ")
    if text == None:
        exit(2)
    print("ciphertext: ", end="")
    for i in text:
        if i.isupper():
            print(chr((ord(i)-65+key)%26+65), end="")
        elif i.islower():
            print(chr((ord(i)-97+key)%26+97), end="")
        else:
            print(i, end="")
    print("")
    exit(0)
if __name__ == "__main__":
    main()
