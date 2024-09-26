first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zipped_list = zip(first, second)
first_result = (int(len(x[0])) - int(len(x[1])) for x in zipped_list
                 if int(len(x[0])) != int(len(x[1])))
print(list(first_result))


first_result = (int(len(first[x])) == int(len(second[x])) for x in range(int(len(first))))
print(list(first_result))







