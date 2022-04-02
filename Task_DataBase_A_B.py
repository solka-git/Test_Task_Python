from string import ascii_lowercase, ascii_uppercase, digits
from random import choices
import csv

# Task_1_A


def task_a(file):
    letters_and_digits = ascii_lowercase + ascii_uppercase + digits

    with open(file, "w") as csv_file:
        for i in range(1024):
            for j in range(6):
                csv_file.write(''.join(choices(letters_and_digits, k=8)) + " ")
            csv_file.write("\n")


file_path = "result_task_A.csv"
task_a(file_path)


# Task_1_B

def vowel_in_row(row):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return row[0] in vowels


def task_b(file1, file2):
    with open(file1, "r", newline='') as read_file:
        with open(file2, "w") as write_file:
            reader = csv.reader(read_file)
            for row in reader:
                flag_print = True
                list_item = (str(row).split(' '))
                row_new = []
                for item in list_item:
                    item_new = item.replace("[", "").replace("]", "").replace("\'", "")
                    item_row = ''
                    for i in item_new:
                        if i.isdigit():
                            if int(i) % 2 == 0:
                                i = '#'
                        item_row += i
                    index = None
                    if item_row != '':
                        if vowel_in_row(item_row):
                            index = list_item.index(item)
                        if index != None:
                            flag_print = False
                        else:
                            row_new.append(item_row)
                if flag_print:
                    for i in row_new:
                        write_file.write(i + ' ')
                    write_file.write('\n')


file_read = "result_task_A.csv"
file_write = "result_task_B.csv"

task_b(file_read, file_write)

