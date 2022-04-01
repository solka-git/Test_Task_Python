from string import ascii_lowercase, ascii_uppercase, digits
from random import choices

letters_and_digits = ascii_lowercase + ascii_uppercase + digits

with open("test_task_A.csv", "w") as csv_file:
    for i in range(1024):
        for j in range(6):
            csv_file.write(''.join(choices(letters_and_digits, k=8)) + " ")
        csv_file.write("\n")

