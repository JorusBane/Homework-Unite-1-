print("Впишите первое число: ")
first = int(input())
print("Впишите второе число: ")
second = int(input())
print("Впишите третье число: ")
third = int(input())
print("Количество одинаковых чисел: ")
if  first == second == third :
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
