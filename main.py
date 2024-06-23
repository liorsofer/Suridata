import json
import random
import multiprocessing as mp


# will randomize the employees order
def randomize_employees(emps: list):
    random.shuffle(emps)


# will read and return the data from the json file
def read__data():
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num_processes = mp.cpu_count()

    emps = []
    read_and_filter_data(emps)
    # print(emps)
    randomize_employees(emps)
    # print(emps)
    print(dwarf_giant_couples(emps))
