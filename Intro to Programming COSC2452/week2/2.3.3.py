guess = [1, 2, 7, 10, 13, 17, 19, 7, 3, 36, 5]
for x in guess:
    if x > 18:
        print(x,"is the winning number")
        break
    else:
        print(x, "is not a winner")
