my_dict = {"Арсений Субботин" : 89229000929, "Валентин Оглобля" : 89514056193}
print(my_dict)
print(my_dict["Арсений Субботин"])
my_dict["Валентина Рыжий хвост"] = 89120332929
print(my_dict)
my_dict.update({"Васильев Золотой" : 89990002123,
                "Злата Новгородская" : 899123102312})
print(my_dict)
Impostor = my_dict.pop("Валентин Оглобля")
print(Impostor)
print(my_dict)

my_set = {"R","R","R","A","M","P","A","G","E",1,1,1}
print(my_set)
my_set.add("E")
my_set.add("Z")
print(my_set)
my_set.remove(1)
print(my_set)
