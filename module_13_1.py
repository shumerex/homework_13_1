import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}-й шар')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    participants = [
        ("Иван", 2),
        ("Алексей", 3),
        ("Богдан", 5)
    ]

    task = []
    for name, power in participants:
        task.append(start_strongman(name, power))

    await asyncio.gather(*task)

asyncio.run(start_tournament())