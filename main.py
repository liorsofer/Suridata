import json
import random
import multiprocessing as mp


# will randomize the employees order
def randomize_employees(emps: list):
    random.shuffle(emps)
    return emps


# will read and return the data from the json file
def read_data():
    # Python program to read json file

    # Load data from JSON file
    with open('files/data.json', 'r') as f:
        data = json.load(f)

    return data


# filter the duplications
def filter_data(data):
    temp_chunk_emp = []
    for item in data:
        if item not in temp_chunk_emp:
            temp_chunk_emp.append(item)

    return temp_chunk_emp


# merge couples for the dwarf giant game
def dwarf_giant_couples(emps: list) -> list[tuple]:
    couples = []

    for i in range(len(emps) - 1):
        couple = (emps[i].get('name'), emps[i + 1].get('name'))
        couples.append(couple)

    # handles the first and last employees
    couple = (emps[len(emps) - 1].get('name'), emps[0].get('name'))
    couples.append(couple)

    return couples


# gets the data and split it into chunks based on how many processes we got
def chunk_data(data, processes):
    return [data[i::processes] for i in range(processes)]


if __name__ == '__main__':
    num_processes = mp.cpu_count() or 1
    # read data from json and split into chunks based on the processes count
    data = read_data()
    chunks = chunk_data(data, num_processes)

    with mp.Pool(processes=num_processes) as pool:
        # Filter duplicates in chunks
        filtered_chunks = pool.map(filter_data, chunks)

        # need to remove duplicates again after merging the chunks
        filtered_data = [item for sublist in filtered_chunks for item in sublist]
        filtered_data = filter_data(filtered_data)

        # now we can chunk the filtered data
        chunks = chunk_data(filtered_data, num_processes)
        randomized_chunks = pool.map(randomize_employees, chunks)
        randomized_data = [item for sublist in randomized_chunks for item in sublist]
        couples_chunks = pool.map(dwarf_giant_couples, randomized_chunks)
        all_couples = [item for sublist in couples_chunks for item in sublist]

    print(all_couples)
