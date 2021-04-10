import json
import ast

big_dict = {}
branch_dict = {'dec': 27, 'bph':50, 'bms':38, 'bma':50, 'bme':123, 'bar':58, 'bec':117, 'bce':122, 'bch':76, 'bcs':125, 'bee':125, 'dcs':27}

for branch in branch_dict:
    file_path = "D:\Documents\Code\Python\gradesScraper\\" + branch + ".json"
    file = open(file_path)
    content = file.read()
    dict = ast.literal_eval(content)
    file.close()

    for student in dict:
        big_dict[student] = dict[student]

a_file = open("D:\Documents\Code\Python\gradesScraper\collective.json", "w")
json.dump(big_dict, a_file)
a_file.close()

print(len(big_dict))
