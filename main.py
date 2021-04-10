from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import ast

branch_dict = {'bph':50, 'bms':38, 'bma':50, 'bme':123}
driver = webdriver.Firefox()

for branch in branch_dict:

    start = time.time()
    write_file = "D:\Documents\Code\Python\gradesScraper\\" + branch + ".json"

    try:
        file1 = open(write_file, "r")
        contents1 = file1.read()
        roll_dict = ast.literal_eval(contents1)
        file1.close()
    except:
        roll_dict = {}

    try:
        for i in range(1, branch_dict[branch]+1):

            tables_arr = []
            subject_dict = {}
            roll_no = "20" + branch + '{0:03}'.format(i)

            driver.get("http://59.144.74.15/scheme20/studentresult/details.asp")

            login = driver.find_element_by_name('RollNumber')
            login.clear()
            login.send_keys(roll_no)
            login.send_keys(Keys.RETURN)

            time.sleep(3)

            try:
                driver.find_element_by_tag_name("h2")
                print(roll_no + " Doesn't exist!")

            except:
                tables = driver.find_elements_by_class_name("ewTable")

                for item in tables:
                    thing = item.text.split("\n")
                    tables_arr.append(thing)

                for i in tables_arr[1][1:]:
                    arr = i.split(" ")
                    subject_dict[str(arr[-4])] = [int(arr[-3]), int(arr[-1])]

                roll_dict[roll_no] = subject_dict
                print(roll_no + " done!")
                time.sleep(5)

            finally:
                driver.back()

        end = time.time()
        print('This operation took: ' + str(end-start))

        a_file = open(write_file, "w")
        json.dump(roll_dict, a_file)
        a_file.close()

    except:
        a_file = open(write_file, "w")
        json.dump(roll_dict, a_file)
        a_file.close()
