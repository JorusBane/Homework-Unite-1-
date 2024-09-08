team1_num = 5
team2_num = 6
print("В команде Мастера кода участников : %(team1_num)s" % {"team1_num" : "5"})
print("Итого сегодня в командах участников : %(team1_num)s и %(team2_num)s" % {"team1_num" : "5",
                                                                               "team2_num" : 6})
score_2 = 42
print("Команда Волшебники данных решила задач: {score_2} !".format(score_2 = "42"))
time1_time = 18015.2
print("Волшебники данных решили задачи за {time1_time}с".format(time1_time = "18015.2"))
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач")
challenge_result = 'Победа команды Волшебники данных!'
print(f"Резельтат битвы: {challenge_result}")
tasks_total = 82
time_avg = 45.2
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")