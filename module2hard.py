import random
Pass = ""
my_list = []
count = random.randint(3, 20)
print(f"Первая ячейка : {count}")
for brut in range(1, count):
    for brut1 in range(brut, count):
        if count % ( brut1 + brut )== 0 and brut != brut1:
           Pass += str(brut) + str(brut1)
print(Pass)
