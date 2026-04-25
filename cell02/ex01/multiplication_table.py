#!/usr/bin/env python3

try:
    print("Enter a number")
    num = int(input())

    i = 0

    while i < 10:
        result = i * num
        print(str(i) + " x " + str(num) + " = " + str(result))
        
        i = i + 1

except EOFError:
    pass
except:
    pass
