from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import ast

#branch_dict = {'bph':50, 'bms':38, 'bma':50, 'bme':123}
branch_dict = (45,55) #45 and 55 are also branches but fuck them lol

driver = webdriver.Firefox()
#driver.get("http://59.144.74.15/scheme20/studentresult/details.asp") #my year
driver.get("http://59.144.74.15/scheme19/studentresult/details.asp") #senior year

for branch in branch_dict:

    start = time.time()
    write_file = "D:\Documents\Code\Python\gradesScraper\\" + str(branch) + ".json"
    error_arr = [0,0,0,0]
    # this block is neccesary in case the internet goes out
    try:
        file1 = open(write_file, "r")
        contents1 = file1.read()
        roll_dict = ast.literal_eval(contents1)
        file1.close()
        print(roll_dict)
    except:
        roll_dict = {}
        print(roll_dict)

    try: # this try block is needed in case the internet goes out or the computer goes to sleep
        #the for loop if I wanna iterate over a dictionary
        '''for i in range(1, branch_dict[branch]+1): #make this a while loop , which is dependent on error_arr
            if error_arr == [1,1,1,1]:
                break'''
        roll = 1
        while error_arr != [1,1,1,1]:

            tables_arr = []
            subject_dict = {}
            roll_no = "19" + str(branch) + '{0:02}'.format(roll)

            login = driver.find_element_by_name('RollNumber')
            login.clear()
            login.send_keys(roll_no)
            login.send_keys(Keys.RETURN)

            time.sleep(3) #implement explicit waiting

            try:
                driver.find_element_by_tag_name("h2")
                print(roll_no + " Doesn't exist!")
                error_arr[roll%4] = 1

            except:
                error_arr[roll%4] = 0
                tables = driver.find_elements_by_class_name("ewTable")
                for item in tables:
                    thing = item.text.split("\n")
                    tables_arr.append(thing)

                try:
                    j = 1
                    while True:
                        for i in tables_arr[j][1:]:
                            arr = i.split(" ")
                            subject_dict[str(arr[-4])] = [int(arr[-3]), int(arr[-1])]
                        j += 2

                except Exception as e:
                    #print(e)
                    roll_dict[roll_no] = subject_dict
                    print(roll_no + " done!")
                    time.sleep(3)

            finally:
                driver.back()
                roll += 1

        end = time.time()
        print('This operation took: ' + str(end-start))
        a_file = open(write_file, "w")
        json.dump(roll_dict, a_file)
        a_file.close()

    except Exception as e:
        print(e)
        end = time.time()
        print('This operation took: ' + str(end-start))
