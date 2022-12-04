import csv
import re

with open('phonebook_raw.csv') as file1:
    all_data = list(csv.reader(file1))
    final_data = list()
    pattern1 = r"(\+7|8)\s*(\(|\s*|\-)(\d+)(\)|\s*|\-)\s*(\d{3})(\-|\s*)(\d{2})(\-|\s*)(\d{2})\s+(\(|\s*)\w+(\.|\s*)\s*(\d+)(\)|\s*)"
    pattern2 = r"(\+7|8)\s*(\(|\s*|\-)(\d+)(\)|\s*|\-)\s*(\d{3})(\-|\s*)(\d{2})(\-|\s*)(\d{2})"
    sub1 = r"+7(\3)\5-\7-\9 доб.\12"
    sub2 = r"+7(\3)\5-\7-\9"
    for row in all_data:
        result_sub_num_1 = re.sub(pattern1, sub1, row[-2])
        row[-2] = result_sub_num_1
    for row in all_data:
        result_sub_num_2 = re.sub(pattern2, sub2, row[-2])
        row[-2] = result_sub_num_2
    for row in all_data:
        if row[0].count(' ') == 2:
            lname_1 = row[0].split(' ')[0]
            fname_1 = row[0].split(' ')[1]
            sname_1 = row[0].split(' ')[2]
            row[0] = lname_1
            row[1] = fname_1
            row[2] = sname_1
        if row[0].count(' ') == 1:
            lname_2 = row[0].split(' ')[0]
            fname_2 = row[0].split(' ')[1]
            row[0] = lname_2
            row[1] = fname_2
    for row in all_data:
        if row[1].count(' ') == 1:
            fname_3 = row[1].split(' ')[0]
            sname_3 = row[1].split(' ')[1]
            row[1] = fname_3
            row[2] = sname_3
    set_for_delete = set()
    for i in range(0, len(all_data)):
        for j in range(1, len(all_data)):
            if (all_data[i][0] + ' ' + all_data[i][1] == all_data[j][0] + ' ' + all_data[j][1]) and (i != j):
                if (i not in set_for_delete) and (j not in set_for_delete):
                    set_for_delete.add(j)
                for y in range(2, len(all_data[0])):
                    if all_data[i][y] == '' or all_data[j][y] == '':
                        all_data[i][y] = all_data[i][y] + all_data[j][y]
    for i in range(0, len(all_data)):
        if i not in set_for_delete:
            final_data.append(all_data[i])

    with open('new.csv', 'w') as file2:
        writer = csv.writer(file2)
        for row in final_data:
            writer.writerow(row)
