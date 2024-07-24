import random
Pass =[]
list = []
res = []
top = []
bot = []
firts_count = random.randint(3, 20)
print(f"Первая ячека : {firts_count}")
for i in range(1,21):
    if i != firts_count:
        list.append(i)
print(list)
for brut in list:
    for brut1 in list:
       # if (firts_count % (brut + brut1) == 0):
            print(brut)
            print(brut1)
    break
