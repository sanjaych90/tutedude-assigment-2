numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']

num = input("Please enter a number: ")
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