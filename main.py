import json
import random


# will randomize the employees order
def randomize_employees(emps: list):
    random.shuffle(emps)


# will read the data from the json file and filter duplicate employees
def read_and_filter_data(emps: list):
    # Python program to read json file

    # Load data from JSON file
    with open('files/data.json', 'r') as f:
        data = json.load(f)

    for item in data:
        if item not in emps:
            emps.append(item)


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
    emps = []
    read_and_filter_data(emps)
    # print(emps)
    randomize_employees(emps)
    # print(emps)
    print(dwarf_giant_couples(emps))
