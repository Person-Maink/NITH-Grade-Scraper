import json
import ast
import matplotlib.pyplot as plt
import numpy as np

file = open("D:\Documents\Code\Python\gradesScraper\\20sem1\collective.json", "r")
contents = file.read()
main_dict = ast.literal_eval(contents)
file.close()

freq_arr = []
sub_dict = {}

for student in main_dict:
    for subject in main_dict[student]:
        sub_dict[subject] = []

for student in main_dict:
    summ = 0
    for subject in main_dict[student]:
        summ += main_dict[student][subject][1]
        sub_dict[subject].append(main_dict[student][subject][1])

    if student[4] == "r":
        freq_arr.append(summ/26)
    else:
        freq_arr.append(summ/24)
    if (summ/24 <= 10) and (summ/24 >= 9.5):
        print(student)

print(len(freq_arr))

thing = 0

for cg in freq_arr:
    if cg < 9.2:
        thing += 1
print(thing/len(freq_arr))

i = 1
'''for subject in sub_dict:
    plot = plt.figure(i)
    print(int(np.max(sub_dict[subject])))
    print(sub_dict[subject])
    plt.hist(sub_dict[subject], bins = int(np.max(sub_dict[subject])))
    plt.title(subject)
    i += 1'''

plot = plt.figure(len(sub_dict)+2)
plt.hist(freq_arr, bins = 30)
plt.title("Cummulative")
plt.show()
