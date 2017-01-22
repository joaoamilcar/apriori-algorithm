import csv


def parse_to_str_dict(filename):
    count = 1
    dataset = {}

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dataset[count] = row
            count += 1

    return dataset

def parse_to_int_dict(filename):
    dataset = parse_to_str_dict(filename)

    # convert str to int
    for key, value in dataset.items():
        for position in range(len(value)):
            value[position] = int(value[position])

    return dataset


