import datetime
import multiprocessing

def read_info(names):
    all_data = []
    with(open(names, 'r', encoding='utf-8') as file):
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line)


start = datetime.datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
for file in filenames:
    read_info(file)
end = datetime.datetime.now() - start
print(end)

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now() - start
    print(end)
