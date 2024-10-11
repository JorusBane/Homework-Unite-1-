import datetime
import multiprocessing

def read_info(names):
    all_data = []
    for obj in names:
        with(open(obj, 'r', encoding='utf-8') as file):
            # for line in file:
            #     # all_data.append(line.readline())
            #     all_data.append(line)
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line)


start = datetime.datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
read_info(filenames)
end = datetime.datetime.now() - start
print(end)


start = datetime.datetime.now()
with multiprocessing.Pool(processes=4) as pool:
    pool.map(read_info, filenames)
end = datetime.datetime.now() - start
print(end)