import csv
from selenium import webdriver
import json

UserInput = "http://www.tgju.org/chart/sekee/2"

driver = webdriver.Chrome('./chromedriver')

# open the website
driver.get(UserInput)
driver.implicitly_wait(25)

cc = 0
for z in range(100000000):
    cc = cc + 1
FinalRes = []
driver.implicitly_wait(5)
Result = driver.find_elements_by_class_name(" close-price")
print(Result[0].text)

for i in range(len(Result)):
    FinalRes.append(Result[i].text)

for i in range(104):
    # nextPageButton = driver.find_elements_by_css_selector("#DataTables_Table_0_next")
    nextPageButton = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_next"]')
    # print(len(nextPageButton))
    driver.implicitly_wait(5)
    nextPageButton.click()
    newResult = driver.find_elements_by_class_name(" close-price")
    print(len(newResult))
    for j in range(len(newResult)):
        FinalRes.append(newResult[j].text)
    # Result.extend(newResult)

    # nextPageButton.click()

# print(len(Result))
print(type(Result))
with open("file.txt", "w") as f:
    for s in FinalRes:
        f.write(s + "\n")

# for i in range(len(Result)):
#     print(Result[i].text)
# FinalRes.append(Result[i].text)
# print(len(FinalRes))

print(len(FinalRes))

# driver.close()

# with open("output.csv", "w", newline="") as f:  # open("output.csv","wb") for Python 2
#     cw = csv.writer(f)
#     cw.writerows(r + [""] for r in FinalRes)
