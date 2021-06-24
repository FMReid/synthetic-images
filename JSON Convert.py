import json
import csv

def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = []
        for i in item.keys():
            leaves.extend(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = []
        for i in item:
            leaves.extend(get_leaves(i, key))
        return leaves
    else:
        return [(key, item)]


with open('annotations.json') as f_input, open('training_set_final_wh.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    write_header = True

    for entry in json.load(f_input):
        leaf_entries = sorted(get_leaves(entry))

        if write_header:
            csv_output.writerow([k for k, v in leaf_entries])
            write_header = False

        csv_output.writerow([v for k, v in leaf_entries])