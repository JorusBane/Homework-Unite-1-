import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for ball in range(1,6):
        print(f'Силач {name} поднял {ball}')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закорнчил выступление ')

async def run():
    print("Start")
    player1 = asyncio.create_task(start_strongman("Анатолий", 10))
    player2 = asyncio.create_task(start_strongman("Василий", 15))
    player3 = asyncio.create_task(start_strongman("Валера", 6))
    await player1
    await player2
    await player3
    print("Finish")

asyncio.run(run())