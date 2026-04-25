#!/usr/bin/env python3

def main():
    first_num = input("Give me the first number: ")
    second_num = input("Give me the second number: ")
    
    num1 = int(first_num)
    num2 = int(second_num)
    
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
    print(f"{num1} * {num2} = {num1 * num2}")

if __name__ == "__main__":
    main()
