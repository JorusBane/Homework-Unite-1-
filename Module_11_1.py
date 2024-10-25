import requests
import pandas as pd
import numpy as np
from pprint import pprint
from faker import  Faker


# params = {"ll": "61.384489,55.188515",
#           "spn": "0.03,0.03",
#           "l": "map"}
# response = requests.get("https://static-maps.yandex.ru/1.x/", params=params)
# print(response)
# with open("map.png", "wb") as file:
#     file.write(response.content)

fake = Faker(["ru_RU"])
print(fake.name())

dates = pd.date_range("20241001", periods=10)
print(dates)
name =[fake.name() for x in range(10)]
df = pd.DataFrame(np.random.randn(10, 10), index=dates, columns=name)
pprint(df)
pprint(df.index)
pprint(df.columns)
