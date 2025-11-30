exceptions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", "/", "\\", "[", "]", "{", "}", "+", "=", "_", "(", ")", "*", "&", "^", "<", ">", "%", "$", "#", "@", "!", "`", "~", "'", ":", '"', " "]

flag = True

for i in num:
    if i not in numbers:
        print("Please enter only integers")
        flag = False
        break

if flag:
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")