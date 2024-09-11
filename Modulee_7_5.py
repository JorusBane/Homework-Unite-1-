import os
import datetime
import time

print("Текущая дериктория -  ", os.getcwd())
if os.path.exists("New ideal world"):
    os.chdir("New ideal world")
else:
    os.mkdir("New ideal world")
    os.chdir("New ideal world")
print("Текущая дериктория -  ", os.getcwd())
#os.makedirs(r"New ideal world\Russian\Chelyabinsk")
print("Текущая дериктория -  ", os.getcwd())
os.path.isdir("Chelyabinsk")
print(os.listdir())
for i in os.walk("."):
    print(i)
os.chdir(r"C:\Users\Owin\PycharmProjects\Homework-Unite-1-")
print("Текущая дериктория -  ", os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(file)
print(dirs)
print(os.stat(file[-1]))
for f in file:
    print("Обнаружен файл ", f)
    time_of_txt = os.path.getctime(f)
    print("Дата создания: ", time.ctime(time_of_txt))
    print("Размер файла: ", os.path.getsize(f))
    print("Путь: ", os.path.join(os.getcwd(), f))
    print("Родительская директория: ",os.path.dirname(os.path.join(os.getcwd(), f)))
