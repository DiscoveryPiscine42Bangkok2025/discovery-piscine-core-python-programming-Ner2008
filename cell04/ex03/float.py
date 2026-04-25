#!/usr/bin/env python3

def main():
    try:
        user_input = input("Give me a number: ")
        num = float(user_input)
        
        if num == int(num):
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    main()
